/**
 * Popup script - Displays status and latest job info
 */

// Check server status
async function checkServerStatus() {
  const indicator = document.getElementById('server-indicator');
  const statusText = document.getElementById('server-status');

  try {
    const response = await fetch('http://46.202.93.22:5000/health', {
      method: 'GET',
      signal: AbortSignal.timeout(2000)
    });

    if (response.ok) {
      indicator.classList.add('active');
      indicator.classList.remove('inactive');
      statusText.textContent = 'Running';
    } else {
      throw new Error('Server not responding');
    }
  } catch (error) {
    indicator.classList.add('inactive');
    indicator.classList.remove('active');
    statusText.textContent = 'Offline';
  }
}

// Load latest job data
function loadLatestJob() {
  chrome.storage.local.get(['latestJob', 'latestCoverLetter', 'timestamp'], (result) => {
    const container = document.getElementById('latest-job-container');

    if (result.latestJob && result.latestCoverLetter) {
      const job = result.latestJob;
      const timestamp = new Date(result.timestamp);
      const timeAgo = getTimeAgo(timestamp);

      container.innerHTML = `
        <div class="latest-job">
          <h3>Latest Generated Letter</h3>
          <div class="job-title">${job.title || 'Untitled Job'}</div>
          <div class="job-meta">${timeAgo}</div>
          <button class="btn btn-primary" id="copy-btn">
            📋 Copy Cover Letter
          </button>
          <button class="btn" id="view-btn">
            👁️ View Full Letter
          </button>
        </div>
      `;

      // Add event listeners
      document.getElementById('copy-btn').addEventListener('click', () => {
        navigator.clipboard.writeText(result.latestCoverLetter);
        const btn = document.getElementById('copy-btn');
        btn.textContent = '✅ Copied!';
        setTimeout(() => {
          btn.textContent = '📋 Copy Cover Letter';
        }, 2000);
      });

      document.getElementById('view-btn').addEventListener('click', () => {
        // Open a new tab with the cover letter
        chrome.tabs.create({
          url: chrome.runtime.getURL('viewer.html')
        });
      });
    } else {
      container.innerHTML = `
        <div class="empty-state">
          <p>No cover letters generated yet.</p>
          <p>Visit an Upwork job page to get started!</p>
        </div>
      `;
    }
  });
}

// Get time ago string
function getTimeAgo(date) {
  const seconds = Math.floor((new Date() - date) / 1000);

  if (seconds < 60) return 'Just now';
  if (seconds < 3600) return `${Math.floor(seconds / 60)} minutes ago`;
  if (seconds < 86400) return `${Math.floor(seconds / 3600)} hours ago`;
  return `${Math.floor(seconds / 86400)} days ago`;
}

// Load jobs count
function loadJobsCount() {
  chrome.storage.local.get(['jobsCount'], (result) => {
    document.getElementById('jobs-count').textContent = result.jobsCount || 0;
  });
}

// Initialize
document.addEventListener('DOMContentLoaded', () => {
  checkServerStatus();
  loadLatestJob();
  loadJobsCount();

  // Refresh server status every 5 seconds
  setInterval(checkServerStatus, 5000);
});
