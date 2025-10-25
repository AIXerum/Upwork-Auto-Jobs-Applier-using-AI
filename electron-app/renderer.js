/**
 * Electron Renderer Process
 * UI logic and IPC communication
 */

const { ipcRenderer } = require('electron');

// State
let browserLaunched = false;
let jobsProcessed = 0;
let currentCoverLetter = '';

// Elements
const launchBtn = document.getElementById('launch-btn');
const closeBrowserBtn = document.getElementById('close-browser-btn');
const extractBtn = document.getElementById('extract-btn');
const copyBtn = document.getElementById('copy-btn');
const searchQueryInput = document.getElementById('search-query');
const coverLetterTextarea = document.getElementById('cover-letter');
const activityLog = document.getElementById('activity-log');
const loadingDiv = document.getElementById('loading');
const jobInfoDiv = document.getElementById('job-info');

// Check Python server status
async function checkServerStatus() {
  const result = await ipcRenderer.invoke('check-server');
  const indicator = document.getElementById('server-indicator');
  const text = document.getElementById('server-text');

  if (result.status === 'online') {
    indicator.className = 'indicator online';
    text.textContent = 'Online';
    logActivity('✅ Python server connected');
  } else {
    indicator.className = 'indicator offline';
    text.textContent = 'Offline';
    logActivity('⚠️ Python server offline - Please run extension_server.py');
  }
}

// Launch browser
launchBtn.addEventListener('click', async () => {
  launchBtn.disabled = true;
  launchBtn.textContent = 'Launching...';

  const searchQuery = searchQueryInput.value.trim() || 'AI Developer';
  const url = `https://www.upwork.com/nx/search/jobs?q=${encodeURIComponent(searchQuery)}&sort=recency`;

  logActivity(`🚀 Launching browser for: ${searchQuery}`);

  const result = await ipcRenderer.invoke('launch-browser', { url });

  if (result.success) {
    browserLaunched = true;
    updateBrowserStatus('online', 'Running');
    extractBtn.disabled = false;
    closeBrowserBtn.disabled = false;
    launchBtn.textContent = 'Browser Launched ✅';
    logActivity('✅ Browser launched successfully');
    logActivity('📝 Login to Upwork and navigate to a job page');
  } else {
    launchBtn.disabled = false;
    launchBtn.textContent = 'Launch Browser';
    logActivity(`❌ Error: ${result.error}`);
    alert(`Failed to launch browser: ${result.error}`);
  }
});

// Close browser
closeBrowserBtn.addEventListener('click', async () => {
  const result = await ipcRenderer.invoke('close-browser');
  if (result.success) {
    browserLaunched = false;
    updateBrowserStatus('offline', 'Not launched');
    extractBtn.disabled = true;
    closeBrowserBtn.disabled = true;
    launchBtn.disabled = false;
    launchBtn.textContent = 'Launch Browser';
    logActivity('🔴 Browser closed');
  }
});

// Extract job and generate cover letter
extractBtn.addEventListener('click', async () => {
  if (!browserLaunched) {
    alert('Please launch browser first');
    return;
  }

  extractBtn.disabled = true;
  extractBtn.textContent = 'Processing...';
  loadingDiv.style.display = 'block';
  jobInfoDiv.style.display = 'none';

  try {
    // Extract job data
    logActivity('🔍 Extracting job data from page...');
    const extractResult = await ipcRenderer.invoke('extract-job');

    if (!extractResult.success) {
      throw new Error(extractResult.error);
    }

    const jobData = extractResult.data;
    logActivity(`📝 Found job: ${jobData.title}`);

    // Generate cover letter
    logActivity('🤖 Generating AI cover letter...');
    const generateResult = await ipcRenderer.invoke('generate-cover-letter', jobData);

    if (!generateResult.success) {
      throw new Error(generateResult.error);
    }

    // Display results
    currentCoverLetter = generateResult.data.cover_letter;
    coverLetterTextarea.value = currentCoverLetter;

    // Show job info
    document.getElementById('job-title').textContent = jobData.title;
    document.getElementById('job-meta').textContent =
      `${jobData.budget || 'N/A'} | ${jobData.experience_level || 'N/A'}`;
    jobInfoDiv.style.display = 'block';

    // Update stats
    jobsProcessed++;
    document.getElementById('jobs-count').textContent = jobsProcessed;

    // Enable copy button
    copyBtn.disabled = false;

    logActivity(`✅ Cover letter generated! (${currentCoverLetter.length} chars)`);
    logActivity('📋 Click "Copy to Clipboard" to use it');

  } catch (error) {
    logActivity(`❌ Error: ${error.message}`);
    alert(`Error: ${error.message}`);
  } finally {
    extractBtn.disabled = false;
    extractBtn.textContent = 'Extract & Generate';
    loadingDiv.style.display = 'none';
  }
});

// Copy to clipboard
copyBtn.addEventListener('click', () => {
  if (!currentCoverLetter) {
    return;
  }

  navigator.clipboard.writeText(currentCoverLetter).then(() => {
    const originalText = copyBtn.textContent;
    copyBtn.textContent = '✅ Copied!';
    setTimeout(() => {
      copyBtn.textContent = originalText;
    }, 2000);
    logActivity('📋 Cover letter copied to clipboard');
  }).catch(err => {
    logActivity(`❌ Copy failed: ${err.message}`);
  });
});

// Update browser status
function updateBrowserStatus(status, text) {
  const indicator = document.getElementById('browser-indicator');
  const textElement = document.getElementById('browser-text');
  indicator.className = `indicator ${status}`;
  textElement.textContent = text;
}

// Log activity
function logActivity(message) {
  const timestamp = new Date().toLocaleTimeString();
  const entry = document.createElement('div');
  entry.className = 'log-entry';
  entry.innerHTML = `<span class="log-time">${timestamp}</span> ${message}`;
  activityLog.insertBefore(entry, activityLog.firstChild);

  // Keep only last 50 entries
  while (activityLog.children.length > 50) {
    activityLog.removeChild(activityLog.lastChild);
  }
}

// Initialize
checkServerStatus();

// Check server status every 5 seconds
setInterval(checkServerStatus, 5000);

// Initial log
logActivity('🎉 App initialized - Ready to generate cover letters!');
