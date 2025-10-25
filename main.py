from dotenv import load_dotenv
from src.utils import read_text_file
from src.graph import UpworkAutomationGraph

# Load environment variables from a .env file
load_dotenv()

if __name__ == "__main__":
    # ========================================================================
    # JOB SEARCH STRATEGY FOR CHRISTOPHER'S PROFILE
    # ========================================================================
    #
    # OPTIMAL JOB TYPES (Based on Upwork profile analysis):
    #
    # TIER 1 - HIGH PRIORITY (Apply to ALL):
    # - "AI Agent Developer" or "AI Chatbot Developer"
    # - "LangChain Developer" or "GPT-4 Developer"
    # - "Voice AI Developer" or "Conversational AI"
    # - "RAG Architecture" or "Vector Database"
    # - "AI + UX" hybrid roles
    #
    # TIER 2 - STRONG FIT (Apply to Most):
    # - "VR Developer Unity" or "VR Training Simulation"
    # - "AR Developer" or "Mixed Reality Developer"
    # - "Spatial Computing" or "Hand Tracking VR"
    #
    # TIER 3 - GOOD FIT (Apply Selectively):
    # - "Full Stack React Python" or "Next.js FastAPI"
    # - "React Native Developer" or "Mobile Full Stack"
    # - "AWS Cloud Architect" or "GCP Developer"
    #
    # TIER 4 - LEVERAGE EXPERIENCE (Only Perfect Matches):
    # - "Senior UX Lead" or "Design Manager"
    # - "Product Design + Development"
    # - Strategic leadership roles with $100K+ budgets
    #
    # ========================================================================
    # SEARCH TIPS:
    # - Apply within first 5 applicants (increases interview rate by 400%)
    # - Target jobs posted in last 24 hours
    # - Look for budgets $50-100+/hr (matches your $85/hr rate)
    # - Prioritize clients with payment verified and good history
    # - Use automation for initial draft, customize first/last paragraphs
    # ========================================================================

    # Job title to search for on Upwork
    # Change this to match optimal job types above
    job_title = "AI Agent Developer"

    # Load the updated freelancer profile
    profile = read_text_file("./files/profile.md")

    # Run automation graph to find jobs and generate cover letters
    bot = UpworkAutomationGraph(profile)
    bot.run(job_title)