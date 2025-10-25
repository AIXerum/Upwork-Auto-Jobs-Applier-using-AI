# Upwork Job Scraping Guide

## The Challenge

Upwork has strong anti-bot protection that blocks automated scraping:
- Returns 403 Forbidden errors
- Requires login/authentication
- Changes page structure frequently
- Detects headless browsers

## Recommended Solutions

### ✅ Option 1: Manual Job Collection (Recommended)

The most reliable approach is to manually collect jobs and use the automation for cover letter generation:

1. **Browse Upwork normally** in your browser
2. **Copy job details** you're interested in
3. **Use the test script** to generate cover letters

**Steps:**

```bash
# 1. Edit test_with_sample_jobs.py and replace sample_jobs with real jobs
# 2. Run the automation
source venv/bin/activate
python test_with_sample_jobs.py
```

**Example job format:**
```python
sample_jobs = [
    {
        'title': 'Your actual job title from Upwork',
        'link': 'https://www.upwork.com/jobs/actual-job-link',
        'description': 'Full job description copied from Upwork',
        'job_type': 'Hourly' or 'Fixed Price',
        'experience_level': 'Entry', 'Intermediate', or 'Expert',
        'budget': 'Actual budget from job posting'
    },
    # Add more jobs...
]
```

###  Option 2: Chrome with Saved Session

Use Chrome with your existing Upwork login:

1. **Login to Upwork** in Chrome normally
2. **Use Selenium with your Chrome profile:**

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
# Use your actual Chrome profile path
options.add_argument("user-data-dir=/Users/chriscarter/Library/Application Support/Google/Chrome")
options.add_argument("profile-directory=Default")

driver = webdriver.Chrome(options=options)
driver.get('https://www.upwork.com/nx/search/jobs?q=AI+Developer')
# Now you're logged in!
```

### Option 3: Upwork RSS Feed

Upwork provides RSS feeds for job searches (no auth needed):

```
https://www.upwork.com/ab/feed/jobs/rss?q=AI+Developer&sort=recency
```

**Pros:**
- No authentication needed
- No scraping required
- Official Upwork feature

**Cons:**
- Limited job details
- May not have full descriptions

### Option 4: Upwork API (If Available)

Check if you can get API access:
- https://developers.upwork.com/
- Requires application approval
- Most official and reliable method

## Current Automation Workflow

Right now, the best workflow is:

1. **Search Upwork manually** → Find jobs you want to apply to
2. **Copy job details** → Paste into test_with_sample_jobs.py
3. **Run automation** → Generates personalized cover letters
4. **Review & submit** → Copy letters back to Upwork proposals

## Quick Start

### Step 1: Find Jobs on Upwork
- Go to https://www.upwork.com
- Search for your target jobs (e.g., "AI Developer", "Full Stack Developer")
- Open jobs you're interested in

### Step 2: Collect Job Data
Copy this information for each job:
- Title
- Link/URL
- Full description
- Budget/rate
- Experience level
- Job type (hourly/fixed)

### Step 3: Generate Cover Letters

Edit `test_with_sample_jobs.py`:

```python
sample_jobs = [
    {
        'title': '[Paste title here]',
        'link': '[Paste link here]',
        'description': '[Paste full description here]',
        'job_type': '[Hourly or Fixed Price]',
        'experience_level': '[Entry/Intermediate/Expert]',
        'budget': '[Paste budget here]'
    },
]
```

Then run:
```bash
source venv/bin/activate
python test_with_sample_jobs.py
```

### Step 4: Use Generated Cover Letters
- Open `files/cover_letter.txt`
- Copy each cover letter
- Paste into Upwork proposal for corresponding job
- Review and submit!

## Tips

1. **Quality over Quantity**: Manually select 5-10 great matches rather than scraping hundreds
2. **Customize**: Always review and tweak generated letters before submitting
3. **Speed**: This workflow is actually faster than setting up complex scraping
4. **Compliance**: Stays within Upwork's terms of service

## Future Enhancements

If you want automated scraping later:
- Upwork API access (requires approval)
- Chrome Extension approach
- Browser automation with manual intervention
- RSS feed parser (limited data but simple)
