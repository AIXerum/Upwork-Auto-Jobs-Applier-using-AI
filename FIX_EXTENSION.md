# 🔧 Fix Chrome Extension Caching Issue

## ⚠️ Problem
Extension is using old cached code with `localhost:5000` instead of production URL `http://46.202.93.22:5000`.

---

## ✅ SOLUTION: Complete Removal & Reinstall

Follow these exact steps:

### Step 1: Remove Old Extension

1. Open: **chrome://extensions/**
2. Find "Upwork Cover Letter Generator"
3. Click **"Remove"** button
4. Confirm removal

### Step 2: Clear Extension Cache (Important!)

1. Open: **chrome://settings/clearBrowserData**
2. Time range: **"All time"**
3. Check **ONLY**: "Cached images and files"
4. Click **"Clear data"**

### Step 3: Close ALL Chrome Windows

1. Quit Chrome completely (Cmd+Q)
2. Wait 3 seconds
3. Reopen Chrome

### Step 4: Install Fresh Extension

1. Open: **chrome://extensions/**
2. Enable **"Developer mode"** (toggle top-right)
3. Click **"Load unpacked"**
4. Navigate to and select:
   ```
   /Users/chriscarter/Documents/GitHub/Upwork-Auto-Jobs-Applier-using-AI/chrome-extension
   ```
5. Click **"Select"**
6. ✅ Extension installed!

### Step 5: Verify Configuration

Open this file in Chrome to test:
```
/Users/chriscarter/Documents/GitHub/Upwork-Auto-Jobs-Applier-using-AI/chrome-extension/test.html
```

Should show:
- **Current API URL**: `http://46.202.93.22:5000` ✅

If it shows `localhost:5000`, the cache wasn't cleared properly.

### Step 6: Test on Upwork

1. Go to: https://www.upwork.com/jobs/Need-span-class-highlight-Full-span-span-class-highlight-Stack-span-Web-Developer-for-business-Website-devlopment_~021979571289927034559/
2. Look for purple button at bottom-right
3. Click it
4. Should now say: "Cannot connect to server at **http://46.202.93.22:5000**" (not localhost!)

---

## 🐛 If Still Not Working

### Check What URL Extension Is Using

1. Open Upwork job page
2. Open DevTools (F12)
3. Go to **Console** tab
4. Type this and press Enter:
   ```javascript
   document.getElementById('upwork-ai-button').onclick.toString()
   ```
5. Look in the code for what API_URL is being used

---

## ⚡ MEANWHILE: Use Paste Script (30 seconds)

Don't wait for extension debugging - get your cover letter NOW:

```bash
cd /Users/chriscarter/Documents/GitHub/Upwork-Auto-Jobs-Applier-using-AI
source venv/bin/activate
python paste_job_url.py
```

Then:
1. Choose option **2**
2. Paste job description from Upwork
3. Press Enter twice
4. ✅ Cover letter copied!
5. Paste in Upwork and apply!

---

## 📊 Why This Happened

Chrome aggressively caches extension files. When you click "Reload" in chrome://extensions, it reloads the extension but may not reload JavaScript files from disk.

**Fix**: Complete removal forces Chrome to load fresh files.

---

## ✅ Success Indicators

After reinstall, you should see:

**In popup:**
- Python Server: ✅ Running (not "Offline")

**In console (F12):**
```
🚀 Upwork Cover Letter Generator extension script loaded
📍 Current URL: https://www.upwork.com/jobs/...
✅ Document already loaded, creating button now
✅ Button created successfully at bottom-right!
```

**Error messages should reference:**
- `http://46.202.93.22:5000` ✅
- NOT `localhost:5000` ❌

---

## 🚀 After Fix

Once working, you can:
- Click button on ANY Upwork job
- Get instant cover letters
- Apply to 10-20 jobs per day
- No local server needed!

---

**Start with the paste script now, then fix extension when you have time!**
