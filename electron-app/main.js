/**
 * Electron Main Process
 * Handles app lifecycle, browser automation, and IPC
 */

const { app, BrowserWindow, ipcMain, dialog } = require('electron');
const path = require('path');
const puppeteer = require('puppeteer-extra');
const StealthPlugin = require('puppeteer-extra-plugin-stealth');
const axios = require('axios');

// Add stealth plugin to avoid bot detection
puppeteer.use(StealthPlugin());

let mainWindow;
let browser;
let page;

// Python server URL
const PYTHON_SERVER = 'http://localhost:5000';

// Create main window
function createWindow() {
  mainWindow = new BrowserWindow({
    width: 1400,
    height: 900,
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false,
      enableRemoteModule: true
    },
    icon: path.join(__dirname, 'icon.png')
  });

  mainWindow.loadFile('index.html');

  // Open DevTools in development
  // mainWindow.webContents.openDevTools();

  mainWindow.on('closed', () => {
    mainWindow = null;
    if (browser) {
      browser.close();
    }
  });
}

// App ready
app.whenReady().then(createWindow);

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('activate', () => {
  if (mainWindow === null) {
    createWindow();
  }
});

// IPC Handlers

// Check Python server status
ipcMain.handle('check-server', async () => {
  try {
    const response = await axios.get(`${PYTHON_SERVER}/health`, {
      timeout: 2000
    });
    return { status: 'online', data: response.data };
  } catch (error) {
    return { status: 'offline', error: error.message };
  }
});

// Launch Puppeteer browser
ipcMain.handle('launch-browser', async (event, config) => {
  try {
    console.log('🚀 Launching browser with stealth mode...');

    // Close existing browser if any
    if (browser) {
      await browser.close();
    }

    // Launch browser with stealth configuration
    browser = await puppeteer.launch({
      headless: false, // Show browser so user can login
      defaultViewport: null,
      args: [
        '--start-maximized',
        '--disable-blink-features=AutomationControlled',
        '--disable-features=IsolateOrigins,site-per-process',
        '--disable-site-isolation-trials',
        '--no-sandbox',
        '--disable-setuid-sandbox',
        '--disable-dev-shm-usage',
        '--disable-accelerated-2d-canvas',
        '--disable-gpu',
        '--window-size=1920,1080'
      ]
    });

    // Get first page
    const pages = await browser.pages();
    page = pages[0] || await browser.newPage();

    // Set extra headers to appear more legitimate
    await page.setExtraHTTPHeaders({
      'Accept-Language': 'en-US,en;q=0.9',
      'Accept-Encoding': 'gzip, deflate, br'
    });

    // Set user agent
    await page.setUserAgent(
      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    );

    // Navigate to Upwork
    const url = config.url || 'https://www.upwork.com/nx/search/jobs?q=AI%20Developer&sort=recency';
    await page.goto(url, {
      waitUntil: 'networkidle2',
      timeout: 30000
    });

    console.log('✅ Browser launched successfully');
    return { success: true, message: 'Browser launched' };

  } catch (error) {
    console.error('❌ Error launching browser:', error);
    return { success: false, error: error.message };
  }
});

// Extract job from current page
ipcMain.handle('extract-job', async () => {
  if (!page) {
    return { success: false, error: 'Browser not launched' };
  }

  try {
    console.log('🔍 Extracting job data...');

    // Extract job data using Puppeteer
    const jobData = await page.evaluate(() => {
      // Find job title
      const titleElement = document.querySelector('h4.text-body-lg, h2.up-n-link') ||
                          document.querySelector('[data-test="job-title"]');
      const title = titleElement ? titleElement.textContent.trim() : '';

      // Find description
      const descElement = document.querySelector('[data-test="Description"]') ||
                         document.querySelector('.break') ||
                         document.querySelector('.job-description');
      const description = descElement ? descElement.innerText.trim() : '';

      // Find budget
      const budgetElement = document.querySelector('[data-test="budget"]') ||
                           document.querySelector('[data-test="hourly-rate"]');
      const budget = budgetElement ? budgetElement.textContent.trim() : '';

      // Find experience level
      const expElement = document.querySelector('[data-test="experience-level"]');
      const experience_level = expElement ? expElement.textContent.trim() : '';

      // Find job type
      const typeElement = document.querySelector('[data-test="job-type"]');
      const job_type = typeElement ? typeElement.textContent.trim() : '';

      return {
        title,
        description,
        budget,
        experience_level,
        job_type,
        link: window.location.href
      };
    });

    console.log('✅ Job data extracted:', jobData.title);
    return { success: true, data: jobData };

  } catch (error) {
    console.error('❌ Error extracting job:', error);
    return { success: false, error: error.message };
  }
});

// Generate cover letter via Python API
ipcMain.handle('generate-cover-letter', async (event, jobData) => {
  try {
    console.log('🤖 Sending to Python server...');

    const response = await axios.post(`${PYTHON_SERVER}/generate-cover-letter`, jobData, {
      timeout: 30000
    });

    console.log('✅ Cover letter generated');
    return { success: true, data: response.data };

  } catch (error) {
    console.error('❌ Error generating cover letter:', error);
    return { success: false, error: error.message };
  }
});

// Navigate to URL
ipcMain.handle('navigate', async (event, url) => {
  if (!page) {
    return { success: false, error: 'Browser not launched' };
  }

  try {
    await page.goto(url, {
      waitUntil: 'networkidle2',
      timeout: 30000
    });
    return { success: true };
  } catch (error) {
    return { success: false, error: error.message };
  }
});

// Take screenshot
ipcMain.handle('screenshot', async () => {
  if (!page) {
    return { success: false, error: 'Browser not launched' };
  }

  try {
    const screenshot = await page.screenshot({ encoding: 'base64' });
    return { success: true, data: screenshot };
  } catch (error) {
    return { success: false, error: error.message };
  }
});

// Close browser
ipcMain.handle('close-browser', async () => {
  if (browser) {
    await browser.close();
    browser = null;
    page = null;
    return { success: true };
  }
  return { success: false, error: 'No browser to close' };
});

console.log('🚀 Electron app ready');
