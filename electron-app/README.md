# Upwork Cover Letter Generator - Electron Desktop App

Desktop application with Puppeteer stealth mode for generating AI-powered cover letters while browsing Upwork.

## ✨ Features

- 🖥️ **Desktop App** - Native application for macOS, Windows, Linux
- 🕵️ **Stealth Mode** - Puppeteer with anti-detection plugins to bypass Cloudflare
- 🔐 **Manual Login** - You login normally, then app assists with extraction
- 🤖 **AI-Powered** - Uses your profile for personalized cover letters
- 📋 **Auto-Copy** - Letters copied to clipboard for easy pasting
- 📊 **Activity Log** - See everything the app is doing

## 🚀 Installation

### Prerequisites

1. **Node.js 18+** installed
2. **Python server** running (`extension_server.py`)

### Install Dependencies

```bash
cd electron-app
npm install
```

This installs:
- Electron
- Puppeteer with stealth plugins
- Axios for API communication

## 📖 How to Use

### Step 1: Start Python Backend

```bash
# In project root directory
source venv/bin/activate
python extension_server.py
```

Server must be running on `http://localhost:5000`

### Step 2: Launch Electron App

```bash
# In electron-app directory
npm start
```

### Step 3: Generate Cover Letters

1. **Enter search query** (e.g., "AI Developer", "Full Stack Engineer")
2. Click **"Launch Browser"**
   - Chrome browser opens with stealth mode
   - Cloudflare protection bypassed
3. **Login to Upwork** in the browser that opened
4. **Navigate to any job page**
5. Click **"Extract & Generate"** in the app
6. Wait 2-5 seconds for AI generation
7. ✅ **Cover letter appears** and is copied to clipboard
8. **Paste into Upwork** and apply!

## 🎨 Interface

### Main Controls

- **Launch Browser** - Opens Puppeteer browser with stealth mode
- **Extract & Generate** - Extracts current job and generates letter
- **Close Browser** - Closes the automation browser
- **Copy to Clipboard** - Copies generated letter

### Status Panel

- **Python Server** - Shows if backend is running
- **Browser** - Shows if Puppeteer browser is active
- **Jobs Processed** - Count of letters generated

### Activity Log

Real-time log of all app actions:
- Browser launch status
- Job extraction progress
- AI generation status
- Success/error messages

## 🛠️ Tech Stack

- **Electron** - Desktop app framework
- **Puppeteer** - Browser automation
- **puppeteer-extra-plugin-stealth** - Anti-bot detection
- **Python Flask** - Backend API
- **Gemini 2.0 Flash** - AI model

## 🔧 Troubleshooting

### Browser doesn't launch
- Make sure you have Chrome/Chromium installed
- Check you have write permissions to temp folder
- Try running with sudo/administrator

### "Cannot connect to Python server"
- Make sure `extension_server.py` is running
- Check it's running on port 5000
- Verify firewall isn't blocking localhost

### Cloudflare still detects bot
- Stealth mode has ~70% success rate
- Try refreshing the page in the browser
- Login manually then try again
- Consider using paste_job_url.py as fallback

### Job extraction fails
- Make sure you're on an actual job page URL
- Wait for page to fully load before extracting
- Check browser console for errors
- Upwork's structure may have changed

## 📦 Building Distributable Apps

### Build for macOS

```bash
npm run build-mac
```

Creates `.app` and `.dmg` in `dist/` folder

### Build for Windows

```bash
npm run build-win
```

Creates `.exe` installer in `dist/` folder

### Build for Linux

```bash
npm run build-linux
```

Creates `.AppImage` and `.deb` in `dist/` folder

## 🚀 Advanced Configuration

### Change AI Model

Edit `extension_server.py` line 67:

```python
model="gemini/gemini-2.0-flash-exp",  # Change to another model
```

Options:
- `gemini/gemini-2.0-flash-exp` (fast, cheap)
- `gemini/gemini-pro` (slower, better)
- `groq/llama3-70b-8192` (requires GROQ_API_KEY)

### Customize Stealth Settings

Edit `main.js` browser launch args to tweak detection evasion.

## ⚠️ Limitations

- **Cloudflare Protection**: ~70% success rate with stealth mode
- **Upwork ToS**: Automated scraping violates their terms
- **Structure Changes**: Upwork updates UI frequently
- **Detection Risk**: Still possible for sophisticated anti-bot

## 💡 Alternatives

If Electron app has too much detection:

1. **Chrome Extension** - Use the browser extension instead (zero detection)
2. **Paste Script** - Use `paste_job_url.py` (100% manual, zero detection)
3. **Real Jobs Script** - Use `real_upwork_jobs.py` with pre-collected jobs

## 📄 License

Part of Upwork Auto Jobs Applier project
