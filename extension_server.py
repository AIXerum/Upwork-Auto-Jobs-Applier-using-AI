"""
Flask server for Chrome Extension
Receives job data from extension and generates cover letters
"""
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from src.utils import read_text_file
from src.agent import Agent
from src.prompts import generate_cover_letter_prompt
import json
import re

load_dotenv()

app = Flask(__name__)
# Enable CORS for Chrome extension and browsers
CORS(app, resources={
    r"/*": {
        "origins": "*",
        "methods": ["GET", "POST", "OPTIONS"],
        "allow_headers": ["Content-Type"],
        "expose_headers": ["Content-Type"],
        "supports_credentials": False
    }
})

# Load profile once on startup
print("📋 Loading profile...")
profile = read_text_file("./files/profile.md")
print(f"✅ Profile loaded ({len(profile)} characters)")

# Initialize AI agent
print("🤖 Initializing AI agent...")
agent = Agent(
    name="Cover Letter Generator",
    model="gemini/gemini-2.0-flash-exp",
    system_prompt=generate_cover_letter_prompt.format(profile=profile),
    temperature=0.1
)
print("✅ Agent ready!")

# Counter for jobs processed
jobs_processed = 0

@app.route('/', methods=['GET'])
def home():
    """Welcome page with API documentation"""
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Upwork Cover Letter Generator API</title>
        <style>
            body {
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: #fff;
                padding: 40px;
                margin: 0;
            }
            .container {
                max-width: 800px;
                margin: 0 auto;
                background: rgba(255, 255, 255, 0.1);
                backdrop-filter: blur(10px);
                border-radius: 20px;
                padding: 40px;
            }
            h1 { margin: 0 0 10px 0; font-size: 36px; }
            .status { color: #4ade80; font-size: 18px; margin-bottom: 30px; }
            .endpoint {
                background: rgba(255, 255, 255, 0.1);
                border-left: 4px solid #4ade80;
                padding: 20px;
                margin: 20px 0;
                border-radius: 8px;
            }
            .endpoint h3 { margin: 0 0 10px 0; }
            .endpoint code {
                background: rgba(0, 0, 0, 0.3);
                padding: 2px 8px;
                border-radius: 4px;
                font-size: 14px;
            }
            .stats {
                display: grid;
                grid-template-columns: repeat(2, 1fr);
                gap: 20px;
                margin-top: 30px;
            }
            .stat {
                background: rgba(255, 255, 255, 0.1);
                padding: 20px;
                border-radius: 12px;
                text-align: center;
            }
            .stat-value { font-size: 32px; font-weight: bold; }
            .stat-label { font-size: 14px; opacity: 0.8; margin-top: 5px; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🤖 Upwork Cover Letter Generator API</h1>
            <div class="status">✅ Server is running</div>

            <p>AI-powered cover letter generation for Upwork jobs using Gemini 2.0 Flash.</p>

            <div class="endpoint">
                <h3>GET /health</h3>
                <p>Health check endpoint</p>
                <code>curl http://46.202.93.22:5000/health</code>
            </div>

            <div class="endpoint">
                <h3>POST /generate-cover-letter</h3>
                <p>Generate personalized cover letter from job data</p>
                <p><strong>Request body:</strong></p>
                <code>
                {
                    "title": "Job Title",
                    "description": "Job description...",
                    "budget": "$50-100/hr",
                    "experience_level": "Expert"
                }
                </code>
            </div>

            <div class="stats">
                <div class="stat">
                    <div class="stat-value">""" + str(jobs_processed) + """</div>
                    <div class="stat-label">Jobs Processed</div>
                </div>
                <div class="stat">
                    <div class="stat-value">✅</div>
                    <div class="stat-label">Status</div>
                </div>
            </div>

            <p style="margin-top: 30px; opacity: 0.7; font-size: 14px;">
                📖 <a href="https://github.com/your-repo" style="color: #fff;">Documentation</a> |
                🔧 <a href="/health" style="color: #fff;">Health Check</a>
            </p>
        </div>
    </body>
    </html>
    """

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'ok',
        'message': 'Server is running',
        'jobs_processed': jobs_processed
    })

@app.route('/generate-cover-letter', methods=['POST'])
def generate_cover_letter():
    """Generate cover letter from job data"""
    global jobs_processed

    try:
        # Get job data from request
        job_data = request.json
        print(f"\n{'='*70}")
        print(f"📥 Received job: {job_data.get('title', 'Unknown')}")
        print(f"{'='*70}")

        # Validate job data
        if not job_data or not job_data.get('description'):
            return jsonify({
                'error': 'Missing job description'
            }), 400

        # Format job description for AI
        job_description = f"{job_data.get('title', '')}\n\n{job_data.get('description', '')}"

        # Add metadata if available
        if job_data.get('budget'):
            job_description += f"\n\nBudget: {job_data['budget']}"
        if job_data.get('experience_level'):
            job_description += f"\nExperience Level: {job_data['experience_level']}"
        if job_data.get('job_type'):
            job_description += f"\nJob Type: {job_data['job_type']}"

        print(f"🤖 Generating cover letter...")
        print(f"⏱️  This takes 2-5 seconds...\n")

        # Generate cover letter
        result = agent.invoke(job_description)

        # Clean up result
        result = re.sub(r'```json\s*', '', result)
        result = re.sub(r'```\s*$', '', result)
        result = result.strip()

        # Parse result
        try:
            result_json = json.loads(result, strict=False)
            cover_letter = result_json.get("letter", result)
        except:
            cover_letter = result

        # Save to file
        with open('./files/cover_letter.txt', 'a', encoding='utf-8') as f:
            f.write(f"\n{cover_letter}\n")
            f.write("-" * 70 + "\n")

        jobs_processed += 1

        print(f"✅ Cover letter generated!")
        print(f"📊 Length: {len(cover_letter)} characters")
        print(f"📈 Total jobs processed: {jobs_processed}")
        print(f"{'='*70}\n")

        return jsonify({
            'success': True,
            'cover_letter': cover_letter,
            'job_title': job_data.get('title'),
            'length': len(cover_letter),
            'jobs_processed': jobs_processed
        })

    except Exception as e:
        print(f"❌ Error: {str(e)}\n")
        return jsonify({
            'error': str(e)
        }), 500

if __name__ == '__main__':
    print("\n" + "="*70)
    print("🚀 UPWORK COVER LETTER GENERATOR - EXTENSION SERVER")
    print("="*70)
    print("\n📡 Starting Flask server on http://localhost:5000")
    print("🔌 Extension can now connect and send jobs\n")
    print("💡 Instructions:")
    print("  1. Install Chrome extension (load unpacked in chrome://extensions)")
    print("  2. Visit any Upwork job page")
    print("  3. Click the floating 'Generate Cover Letter' button")
    print("  4. Cover letter will be copied to clipboard!\n")
    print("="*70 + "\n")

    app.run(host='0.0.0.0', port=5000, debug=True)
