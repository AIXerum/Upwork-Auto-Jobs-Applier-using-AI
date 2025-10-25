/**
 * Upwork Job Application Bookmarklet
 *
 * How to install:
 * 1. Create a new bookmark in your browser
 * 2. Copy ALL the code from upwork_bookmarklet_formatted.txt
 * 3. Paste as the URL of the bookmark
 * 4. Name it: "Apply with AI"
 *
 * How to use:
 * 1. Browse to any Upwork job page
 * 2. Click the "Apply with AI" bookmark
 * 3. Cover letter generates and auto-fills
 * 4. Review and click "Send"
 */

(function() {
    // Extract job details from Upwork page
    function extractJobData() {
        const data = {
            title: '',
            description: '',
            budget: '',
            client_info: '',
            experience_level: '',
            skills: []
        };

        // Get job title
        const titleEl = document.querySelector('h4, h3, h2');
        if (titleEl) data.title = titleEl.textContent.trim();

        // Get job description
        const descEl = document.querySelector('[data-test="Description"], .job-description, .description');
        if (descEl) {
            data.description = descEl.textContent.trim();
        } else {
            // Fallback: get all paragraphs
            const paras = document.querySelectorAll('p');
            data.description = Array.from(paras).map(p => p.textContent).join('\n').trim();
        }

        // Get budget
        const budgetEls = document.querySelectorAll('li, span');
        for (let el of budgetEls) {
            const text = el.textContent;
            if (text.includes('$') && (text.includes('hr') || text.includes('Hourly') || text.includes('Fixed'))) {
                data.budget = text.trim();
                break;
            }
        }

        // Get experience level
        const expEls = document.querySelectorAll('strong, span');
        for (let el of expEls) {
            const text = el.textContent.trim();
            if (text === 'Expert' || text === 'Intermediate' || text === 'Entry Level') {
                data.experience_level = text;
                break;
            }
        }

        // Get client info
        const clientEls = document.querySelectorAll('[data-test="client-info"], .client-info');
        if (clientEls.length > 0) {
            data.client_info = clientEls[0].textContent.trim();
        }

        // Get skills
        const skillButtons = document.querySelectorAll('button[data-test*="skill"], .skill-tag, [href*="skill"]');
        data.skills = Array.from(skillButtons).slice(0, 8).map(s => s.textContent.trim());

        return data;
    }

    // Send to automation server
    async function generateCoverLetter(jobData) {
        try {
            const response = await fetch('http://localhost:5000/generate-cover-letter', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(jobData)
            });

            const result = await response.json();

            if (result.success) {
                return result;
            } else {
                throw new Error(result.message || 'Failed to generate cover letter');
            }
        } catch (error) {
            console.error('Error:', error);
            alert('Error connecting to automation server. Make sure it\'s running:\n\npython automation_server.py');
            throw error;
        }
    }

    // Auto-fill cover letter into Upwork form
    function fillCoverLetter(coverLetter, suggestedRate) {
        // Find cover letter textarea
        const coverLetterField = document.querySelector('textarea[name*="cover"], textarea[placeholder*="cover"], textarea');

        if (coverLetterField) {
            coverLetterField.value = coverLetter;
            coverLetterField.dispatchEvent(new Event('input', { bubbles: true }));
            coverLetterField.dispatchEvent(new Event('change', { bubbles: true }));
            console.log('✅ Cover letter filled');
        } else {
            console.error('❌ Could not find cover letter field');
        }

        // Try to fill hourly rate if suggested
        if (suggestedRate) {
            const rateFields = document.querySelectorAll('input[type="text"], input[type="number"]');
            for (let field of rateFields) {
                const label = field.getAttribute('aria-label') || field.getAttribute('placeholder') || '';
                if (label.toLowerCase().includes('rate') || label.toLowerCase().includes('hourly')) {
                    const rateNum = suggestedRate.replace('$', '').replace('.00', '');
                    field.value = rateNum;
                    field.dispatchEvent(new Event('input', { bubbles: true }));
                    field.dispatchEvent(new Event('change', { bubbles: true }));
                    console.log(`✅ Rate filled: ${suggestedRate}`);
                    break;
                }
            }
        }
    }

    // Main execution
    async function main() {
        // Show loading indicator
        const overlay = document.createElement('div');
        overlay.style.cssText = `
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.3);
            z-index: 999999;
            text-align: center;
            font-family: Arial, sans-serif;
        `;
        overlay.innerHTML = `
            <h3 style="margin: 0 0 15px 0;">🤖 Generating AI Cover Letter...</h3>
            <p style="margin: 0; color: #666;">Using your Microsoft & Home Depot experience</p>
        `;
        document.body.appendChild(overlay);

        try {
            // Extract job data
            const jobData = extractJobData();
            console.log('Job data extracted:', jobData);

            // Generate cover letter
            const result = await generateCoverLetter(jobData);

            // Auto-fill the form
            fillCoverLetter(result.cover_letter, result.suggested_rate);

            // Update overlay
            overlay.innerHTML = `
                <h3 style="margin: 0 0 15px 0; color: #14a800;">✅ Cover Letter Generated!</h3>
                <p style="margin: 0 0 10px 0;">Filled into form. Review and click Send.</p>
                <p style="margin: 0; font-size: 12px; color: #666;">
                    Rate: ${result.suggested_rate || '$85/hr'}<br>
                    Length: ${result.cover_letter.length} chars
                </p>
                <button onclick="this.parentElement.remove()" style="
                    margin-top: 15px;
                    padding: 8px 20px;
                    background: #14a800;
                    color: white;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                    font-size: 14px;
                ">Close</button>
            `;

            // Auto-close after 5 seconds
            setTimeout(() => overlay.remove(), 5000);

        } catch (error) {
            overlay.innerHTML = `
                <h3 style="margin: 0 0 15px 0; color: red;">❌ Error</h3>
                <p style="margin: 0; font-size: 14px;">${error.message}</p>
                <p style="margin: 10px 0 0 0; font-size: 12px; color: #666;">
                    Make sure automation_server.py is running
                </p>
                <button onclick="this.parentElement.remove()" style="
                    margin-top: 15px;
                    padding: 8px 20px;
                    background: #dc3545;
                    color: white;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                ">Close</button>
            `;
        }
    }

    main();
})();
