"""
Local automation server for Upwork job applications
Receives job data from browser, generates cover letters, returns to auto-fill
"""
from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from dotenv import load_dotenv
from src.utils import read_text_file
from src.agent import Agent
from src.prompts import generate_cover_letter_prompt
import re

load_dotenv()

app = Flask(__name__)
CORS(app)  # Allow requests from browser

# Load profile once at startup
profile = read_text_file("./files/profile.md")

# Initialize AI agent
cover_letter_agent = Agent(
    name="Cover Letter Generator",
    model="gemini/gemini-2.5-flash-preview-05-20",
    system_prompt=generate_cover_letter_prompt.format(profile=profile),
    temperature=0.1
)

@app.route('/ping', methods=['GET'])
def ping():
    """Health check endpoint"""
    return jsonify({'status': 'ok', 'message': 'Upwork automation server running'})

@app.route('/generate-cover-letter', methods=['POST'])
def generate_cover_letter():
    """
    Receive job details from browser, generate cover letter

    Expected input:
    {
        "title": "Job title",
        "description": "Full job description",
        "budget": "Budget info",
        "client_info": "Client details"
    }
    """
    try:
        job_data = request.json

        # Format job description for AI
        job_description = f"""
Title: {job_data.get('title', '')}
Budget: {job_data.get('budget', '')}
Client: {job_data.get('client_info', '')}

Description:
{job_data.get('description', '')}
"""

        print(f"\n🎯 Generating cover letter for: {job_data.get('title', 'Unknown')}")
        print(f"📊 Budget: {job_data.get('budget', 'Unknown')}")

        # Generate cover letter using AI
        cover_letter_result = cover_letter_agent.invoke(job_description)

        # Clean up response
        cover_letter_result = re.sub(r'```json\s*', '', cover_letter_result)
        cover_letter_result = re.sub(r'```\s*$', '', cover_letter_result)
        cover_letter_result = cover_letter_result.strip()

        # Parse JSON
        result_json = json.loads(cover_letter_result, strict=False)
        cover_letter = result_json.get("letter", cover_letter_result)

        print(f"✅ Cover letter generated ({len(cover_letter)} characters)")

        # Log application
        with open('./files/application_log.txt', 'a') as f:
            f.write(f"\n{'='*70}\n")
            f.write(f"Job: {job_data.get('title', '')}\n")
            f.write(f"Budget: {job_data.get('budget', '')}\n")
            f.write(f"Generated: {cover_letter}\n")
            f.write(f"{'='*70}\n")

        return jsonify({
            'success': True,
            'cover_letter': cover_letter,
            'suggested_rate': extract_rate_suggestion(job_data.get('budget', '')),
            'message': 'Cover letter generated successfully'
        })

    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return jsonify({
            'success': False,
            'error': str(e),
            'message': 'Failed to generate cover letter'
        }), 500

def extract_rate_suggestion(budget_str):
    """Extract and suggest appropriate bid rate from budget string"""
    budget_lower = budget_str.lower()

    # Extract hourly rates
    if 'hr' in budget_lower or 'hourly' in budget_lower:
        # Try to find numbers
        import re
        numbers = re.findall(r'\$(\d+)', budget_str)
        if len(numbers) >= 2:
            # Take the higher end of the range
            return f"${numbers[-1]}.00"
        elif len(numbers) == 1:
            return f"${numbers[0]}.00"
        return "$85.00"  # Default to profile rate

    # Fixed price - return as-is
    elif 'fixed' in budget_lower:
        numbers = re.findall(r'\$[\d,]+', budget_str)
        if numbers:
            return numbers[0]

    return "$85.00"  # Default

@app.route('/log-application', methods=['POST'])
def log_application():
    """Log successful application"""
    try:
        app_data = request.json

        with open('./files/applications_sent.json', 'a') as f:
            f.write(json.dumps(app_data) + '\n')

        print(f"✅ Logged application: {app_data.get('title', 'Unknown')}")

        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == '__main__':
    print("=" * 70)
    print("🚀 UPWORK AUTOMATION SERVER")
    print("=" * 70)
    print("\n✅ Server starting on http://localhost:5000")
    print("\n📋 Available endpoints:")
    print("  - GET  /ping")
    print("  - POST /generate-cover-letter")
    print("  - POST /log-application")
    print("\n💡 Use the browser bookmarklet to send job data here")
    print("=" * 70 + "\n")

    app.run(debug=False, port=5000, host='127.0.0.1', use_reloader=False)
