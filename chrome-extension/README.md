# Upwork Cover Letter Generator - Chrome Extension

AI-powered Chrome extension that generates personalized cover letters while you browse Upwork jobs.

## ✨ Features

- 🎯 **One-Click Generation** - Click floating button on any Upwork job page
- 📋 **Auto-Copy to Clipboard** - Cover letter instantly copied for pasting
- 🤖 **AI-Powered** - Uses your profile to create personalized letters
- ⚡ **Fast** - Generates letters in 2-5 seconds
- 🔒 **Private** - Runs locally, your data stays on your machine

## 🚀 Installation

### Step 1: Start Python Backend Server

```bash
# Navigate to project directory
cd /Users/chriscarter/Documents/GitHub/Upwork-Auto-Jobs-Applier-using-AI

# Activate virtual environment
source venv/bin/activate

# Start Flask server
python extension_server.py
```

Server will run on `http://localhost:5000`

### Step 2: Install Chrome Extension

1. Open Chrome and go to `chrome://extensions/`
2. Enable "Developer mode" (toggle in top right)
3. Click "Load unpacked"
4. Select the `chrome-extension` folder:
   ```
   /Users/chriscarter/Documents/GitHub/Upwork-Auto-Jobs-Applier-using-AI/chrome-extension
   ```
5. Extension installed! ✅

## 📖 How to Use

1. **Make sure Python server is running** (extension_server.py)
2. Go to Upwork and log in
3. Open any job page (e.g., `https://www.upwork.com/jobs/...`)
4. Look for the **floating purple button** at bottom-right
5. Click **"Generate Cover Letter"**
6. Wait 2-5 seconds...
7. ✅ **Cover letter copied to clipboard!**
8. Paste into Upwork's cover letter field
9. Review, customize if needed, and apply!

## 🎨 Extension UI

### Floating Button
- Appears on every Upwork job page
- Click to generate cover letter
- Shows loading spinner while generating

### Extension Popup
- Click extension icon in Chrome toolbar
- See server status (online/offline)
- View latest generated letter
- Copy previous letters

## 🔧 Troubleshooting

### Button doesn't appear
- Make sure you're on a job page URL like `/jobs/...`
- Refresh the page
- Check if extension is enabled in `chrome://extensions`

### "Cannot connect to server" error
- Make sure `extension_server.py` is running
- Check it's running on `http://localhost:5000`
- Run `python extension_server.py` in terminal

### Cover letter not copying
- Check browser permissions
- Try manually copying from extension popup
- Check console for errors (F12)

## 🛠️ Tech Stack

- **Frontend**: Vanilla JavaScript (Chrome Extension APIs)
- **Backend**: Python Flask server
- **AI**: Gemini 2.0 Flash (via LiteLLM)
- **Storage**: Chrome Storage API

## 📝 Files

```
chrome-extension/
├── manifest.json      # Extension configuration
├── content.js         # Runs on Upwork pages
├── background.js      # Background service worker
├── popup.html         # Extension popup UI
├── popup.js           # Popup logic
├── styles.css         # Button and notification styles
└── README.md          # This file
```

## 🚀 Production Deployment

To deploy the Python backend to Hostinger or other hosting:

1. See `Dockerfile` in project root
2. Build and push Docker container
3. Update `content.js` API_URL to your server URL
4. Reload extension with new URL

## 📄 License

Part of Upwork Auto Jobs Applier project
