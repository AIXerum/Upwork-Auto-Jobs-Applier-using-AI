/**
 * Background service worker
 * Handles extension events and notifications
 */

// Listen for extension install
chrome.runtime.onInstalled.addListener(() => {
  console.log('🎉 Upwork Cover Letter Generator installed!');

  // Show welcome notification
  chrome.notifications.create({
    type: 'basic',
    iconUrl: 'icon48.png',
    title: 'Upwork Cover Letter Generator',
    message: 'Extension installed! Visit any Upwork job page to see the "Generate Cover Letter" button.'
  });
});

// Listen for messages from content script
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.type === 'COVER_LETTER_GENERATED') {
    // Show success notification
    chrome.notifications.create({
      type: 'basic',
      iconUrl: 'icon48.png',
      title: '✅ Cover Letter Ready!',
      message: 'Your cover letter has been generated and copied to clipboard.'
    });
  }

  if (request.type === 'ERROR') {
    // Show error notification
    chrome.notifications.create({
      type: 'basic',
      iconUrl: 'icon48.png',
      title: '⚠️ Error',
      message: request.message || 'An error occurred'
    });
  }
});

console.log('🚀 Background service worker running');
