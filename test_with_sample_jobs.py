"""
Test script with sample Upwork jobs to demonstrate cover letter generation
"""
from dotenv import load_dotenv
from src.utils import read_text_file, save_jobs_to_file
from src.graph import UpworkAutomationGraph

# Load environment variables
load_dotenv()

# Sample Upwork job listings for testing
sample_jobs = [
    {
        'title': 'AI Agent Developer for Customer Support Automation',
        'link': 'https://www.upwork.com/jobs/sample1',
        'description': 'We are looking for an experienced AI developer to build an autonomous customer support agent using LangChain and GPT-4. The agent should handle 80% of customer inquiries automatically. Experience with vector databases and RAG architecture required. Must have portfolio of similar AI agent projects.',
        'job_type': 'Hourly',
        'experience_level': 'Expert',
        'budget': '$50-$100/hr'
    },
    {
        'title': 'Full Stack Developer - React & Python',
        'link': 'https://www.upwork.com/jobs/sample2',
        'description': 'Need a full-stack developer to build a SaaS platform from scratch. Tech stack: React, Next.js, Python FastAPI, PostgreSQL, AWS. The application will have user authentication, payment integration (Stripe), and real-time data synchronization. Looking for someone who can work independently and deliver high-quality code.',
        'job_type': 'Fixed Price',
        'experience_level': 'Expert',
        'budget': 'Fixed price - $8000'
    },
    {
        'title': 'VR Experience Developer for Training Simulation',
        'link': 'https://www.upwork.com/jobs/sample3',
        'description': 'We need a VR developer to create an immersive training simulation for healthcare workers. Unity 3D experience required. Should include hand tracking, haptic feedback, and realistic medical scenarios. Previous work in VR training or medical simulations is a plus.',
        'job_type': 'Fixed Price',
        'experience_level': 'Intermediate',
        'budget': 'Fixed price - $12000'
    }
]

if __name__ == "__main__":
    print("🧪 Testing with sample Upwork jobs...\n")

    # Save sample jobs to file
    save_jobs_to_file(sample_jobs, './files/upwork_job_listings.txt')

    # Load profile
    profile = read_text_file("./files/profile.md")

    # Create bot
    bot = UpworkAutomationGraph(profile, num_jobs=3)

    # Manually run the workflow with sample data
    job_listings_str = "\n".join(map(str, sample_jobs))

    state = {
        "job_title": "AI Developer (Test)",
        "scraped_jobs_list": job_listings_str,
        "matches": [],
        "job_description": "",
        "cover_letter": "",
        "num_matches": 0
    }

    print("✅ Sample jobs loaded")
    print("\n📊 Classifying jobs with AI...")
    state = bot.classify_scraped_jobs(state)

    print("\n🔍 Checking for matches...")
    state = bot.check_for_job_matches(state)

    if len(state['matches']) > 0:
        print(f"\n✅ Found {len(state['matches'])} matching jobs!")
        print("\n✍️  Generating cover letters...\n")

        # Generate cover letters for all matches
        while len(state['matches']) > 0:
            state = bot.generate_cover_letter(state)
            state = bot.save_cover_letter(state)

        print("\n✅ Done! Cover letters saved to: files/cover_letter.txt")
        print("\nYou can now review the generated cover letters.")
    else:
        print("\n⚠️  No matching jobs found")
