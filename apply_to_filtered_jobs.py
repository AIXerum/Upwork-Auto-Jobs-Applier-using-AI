"""
Apply to jobs from Christopher's filtered search (screenshot)
These are the high-value, low-competition jobs with optimal filters
"""
from dotenv import load_dotenv
from src.utils import read_text_file, save_jobs_to_file
from src.graph import UpworkAutomationGraph

load_dotenv()

# Jobs from Christopher's filtered screenshot
# All have: $50+/hr or $1K-$5K+, Expert/Intermediate, Less than 5 proposals
filtered_jobs = [
    {
        'title': 'Complete MVP for AI-Powered Competitor Research SaaS (75% Built)',
        'link': 'https://www.upwork.com/jobs/~[job-id-from-upwork]',
        'description': '''Senior Full Stack Developer: Complete MVP for SaaS Platform (90-Day, Milestone-Based Contract with 1-Week Trial).

We're building an AI-powered competitor research SaaS platform and need an experienced full-stack developer to finalize and launch the MVP. The platform is already 75% built, and we need someone who can jump in, understand the existing architecture, and get us across the finish line efficiently.

Budget: $1.2L/month ($1400 USD/month for 3 months = $4,200 total)
STRUCTURE: 6 fixed-price milestones (€60k INR every 2 weeks)
START: 1-week paid trial

Tech Stack:
- Frontend: React
- Backend: Python
- Database: MongoDB
- AI: LangChain, OpenAI, AI-Generated Code
- Other: Redis, REST API, Tailwind CSS

Requirements:
- Strong experience with React, Python, MongoDB
- Experience with AI integrations (LangChain preferred)
- Can work independently and meet milestone deadlines
- Available to start immediately for 1-week trial

Please include in your proposal:
1. Brief overview of similar SaaS projects you've completed
2. Your approach to understanding existing codebases
3. Availability to start this week
4. Experience with AI/LangChain integrations

Skills Required: React, Python, MongoDB, LangChain, Redis, REST API, Tailwind CSS''',
        'job_type': 'Fixed Price',
        'experience_level': 'Expert',
        'budget': 'Fixed price: $4,200 total (3 months, milestone-based)'
    },
    {
        'title': 'Full Stack Engineer',
        'link': 'https://www.upwork.com/jobs/~[job-id-from-upwork]',
        'description': '''This is a full-time role for a Software Engineer, initially remote but favoring freelancers who would consider an onsite role in San Francisco after 1-2 months.

We will NOT consider any applicants who do not currently have authorization to work in the U.S. You'll design, build, and maintain our product—a platform for creating apps powered by AI-generated code.

Required Skills:
- Full-stack development (React, Node.js, TypeScript)
- Database design and optimization (PostgreSQL preferred)
- API design and integration
- Experience with AI/ML integrations (OpenAI Codex, similar)
- Cloud deployment (AWS/GCP)
- Web application security best practices

Nice to Have:
- Experience with code generation tools
- Understanding of compiler/interpreter design
- Previous startup experience
- Open source contributions

You'll be working with a small, technical team building cutting-edge AI tools. Must be able to work independently and move fast.

Budget: $70-90/hr
Duration: More than 6 months, 30+ hrs/week
Location: Remote initially, then San Francisco

Skills Required: React, Node.js, TypeScript, PostgreSQL, OpenAI Codex, Web Application''',
        'job_type': 'Hourly',
        'experience_level': 'Expert',
        'budget': 'Hourly: $70-90/hr, 6+ months, 30+ hrs/week'
    },
    {
        'title': 'Tutor Needed - Walk Me Through Docker + Google Cloud Deployment (Django/React Project)',
        'link': 'https://www.upwork.com/jobs/~[job-id-from-upwork]',
        'description': '''Project Overview: I have a Django + React application and I want to finalize a local Docker development setup (docker-compose.yml, backend/frontend containers, Postgre SQL). Deploy the app to Google Cloud using Cloud Run and Cloud SQL, with proper secrets, production settings, etc.

I'm looking for someone to TEACH me the process, not just do it for me. We'll work together step-by-step so I understand each part.

What I Need:
- Help me finalize local Docker setup if needed
- Walk me through deploying to Google Cloud (Cloud Run + Cloud SQL)
- Explain best practices for production Django/React deployment
- Show me how to manage secrets, environment variables
- Help troubleshoot any deployment issues

Your Role:
- Screen share and walk me through the process
- Explain WHY we're doing each step (not just HOW)
- Be patient and educational
- Provide documentation/notes I can reference later

Requirements:
- Strong experience with Django, React, Docker, Google Cloud Platform
- Good communicator who enjoys teaching
- Patient and clear explanations
- Available for 2-4 hour sessions over 1-2 weeks

Budget: $60-95/hr
Duration: 1-3 months (but likely just 5-10 hours total)

Skills Required: Python, React, Google Cloud Platform, Docker, Django, PostgreSQL''',
        'job_type': 'Hourly',
        'experience_level': 'Expert',
        'budget': 'Hourly: $60-95/hr, 1-3 months, Less than 30 hrs/week'
    },
    {
        'title': 'Founding Full Stack Engineer (Dual Partnership Model - SaaS + Client-Facing Lead)',
        'link': 'https://www.upwork.com/jobs/~[job-id-from-upwork]',
        'description': '''We're building something different from traditional freelancing. Our Dual Partnership Program gives top engineers the chance to secure long-term remote work while also co-building SaaS products with equity.

As a, you'll just not only be coding—you'll be a partner.

What You'll Do:
- Lead engineering on our flagship SaaS product
- Handle client-facing technical leadership for select enterprise clients
- Build features, architect systems, and own the technical roadmap
- Work with modern stack: React, Python, Node.js, PostgreSQL, AWS
- Collaborate with product team on strategy and vision

What We're Looking For:
- 5+ years full-stack experience
- Strong with React, Python/Node.js, databases
- Experience launching and scaling SaaS products
- Can lead technical conversations with clients
- Startup mindset: ownership, speed, quality
- Strong English communication

The Opportunity:
- Hourly rate: $70-85/hr for client work
- Equity: TBD based on commitment level
- Remote, long-term collaboration
- Potential to grow into CTO/technical co-founder role

If you're interested in building something meaningful (not just doing tickets), let's talk.

Please include:
- Link to a SaaS product you've built
- Your approach to technical leadership
- Interest in equity/partnership model

Skills Required: React, Python, Node.js, JavaScript, SaaS, API, Front-End Development''',
        'job_type': 'Hourly',
        'experience_level': 'Expert',
        'budget': 'Hourly: $70-85/hr + equity, 6+ months, Less than 30 hrs/week'
    },
]

if __name__ == "__main__":
    print("=" * 70)
    print("🎯 APPLYING TO CHRISTOPHER'S FILTERED JOBS")
    print("High-value, low-competition jobs ($50+/hr, <5 proposals)")
    print("=" * 70)

    print(f"\n✅ Found {len(filtered_jobs)} excellent jobs to apply to:")
    for i, job in enumerate(filtered_jobs, 1):
        print(f"\n{i}. {job['title']}")
        print(f"   {job['budget']}")
        print(f"   {job['experience_level']} level")

    print("\n" + "=" * 70)
    print("🚀 Generating AI-powered cover letters...")
    print("=" * 70 + "\n")

    # Save jobs
    save_jobs_to_file(filtered_jobs, './files/upwork_job_listings.txt')

    # Load profile
    profile = read_text_file("./files/profile.md")

    # Create bot
    bot = UpworkAutomationGraph(profile, num_jobs=len(filtered_jobs))

    # Run automation
    job_listings_str = "\n".join(map(str, filtered_jobs))

    state = {
        "job_title": "Filtered High-Value Jobs",
        "scraped_jobs_list": job_listings_str,
        "matches": [],
        "job_description": "",
        "cover_letter": "",
        "num_matches": 0
    }

    print("📊 Classifying jobs...")
    state = bot.classify_scraped_jobs(state)

    print("\n🔍 Checking matches...")
    state = bot.check_for_job_matches(state)

    if len(state['matches']) > 0:
        print(f"\n✅ {len(state['matches'])} jobs matched your profile!")
        print("\n✍️  Generating cover letters...\n")

        # Generate cover letters
        while len(state['matches']) > 0:
            state = bot.generate_cover_letter(state)
            state = bot.save_cover_letter(state)

        print("\n" + "=" * 70)
        print("✅ DONE! Cover letters saved to: files/cover_letter.txt")
        print("=" * 70)

        print("\n📋 NOW:")
        print("1. Open files/cover_letter.txt")
        print("2. Open Upwork in your browser")
        print("3. Apply to each job (copy-paste cover letter)")
        print("4. Customize first sentence for each")
        print("5. Adjust rate to match budget")

        print("\n⏱️  Time to apply to all 4: ~15 minutes")
        print("🎯 You'll have 5 total applications today!")
        print("\n💡 Applications today: 1 done, 4 to go = 5 total ✅")
    else:
        print("\n⚠️  No matches found")
