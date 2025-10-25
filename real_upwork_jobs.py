"""
REAL Upwork Full-Stack Jobs (Extracted: Oct 19, 2025)
Use these with your automation to generate cover letters
"""
from dotenv import load_dotenv
from src.utils import read_text_file, save_jobs_to_file
from src.graph import UpworkAutomationGraph

load_dotenv()

# REAL JOBS FROM UPWORK - Full Stack React Python Search
real_jobs = [
    {
        'title': 'Full Stack Developer for Electron Packaging for windows application',
        'link': 'https://www.upwork.com/jobs/Full-Stack-Developer-for-Electron-Packaging-for-windows-application_~021979601231295668473/',
        'description': '''We are seeking a skilled full stack developer to package our finance productivity desktop application using Electron. The ideal candidate will have experience with Python, React, stripe, and Auth0, and be capable of handling full stack development tasks.

Required Skills: React, Python, Flask, HTML, CSS, JavaScript, GitHub, Electron''',
        'job_type': 'Hourly',
        'experience_level': 'Intermediate',
        'budget': 'Hourly: $50.00 - $70.00, Est. time: 1 to 3 months, 30+ hrs/week'
    },
    {
        'title': 'Full-Stack Developer for Youth Hockey Analytics Platform',
        'link': 'https://www.upwork.com/jobs/Full-Stack-Developer-for-Youth-Hockey-Analytics-Platform_~021979601205251177294/',
        'description': '''We're building a membership-based hockey analytics platform that evaluates youth players using performance stats and physical traits to generate Prospect Scores and Draft Probabilities. Our predictive model is being built by a data scientist who will deliver a clean Python script that takes player stats as input and returns prospect scores and draft probabilities. We're now looking for a full-stack developer to bring the platform to life.

This role will begin with building the MVP, but we're ideally looking for someone interested in a longer-term collaboration. After launch, we'd love to continue working with you for ongoing feature development, maintenance, and platform improvements as the business grows.

🔧 What You'll Build:
- Translating Figma designs into a responsive web and mobile experience
- Building user-facing pages for player search, profiles, and comparisons
- Integrating a Python-based scoring script (provided) to generate player prospect scores
- Connecting to a database for structured player data
- Setting up membership access control

✅ You're a Good Fit If You:
- Have experience building modern, responsive web apps
- Can work with third-party APIs and integrate custom Python scripts
- Know how to handle membership access and feature gating
- Are comfortable collaborating asynchronously

🛠️ Tech Stack (Flexible):
- Frontend: React + TailwindCSS
- Backend: Python (FastAPI) or Node
- Database: Supabase or PostgreSQL
- Auth/Membership: Outseta

💵 Timeline & Budget:
- We aim to launch the MVP in 10-12 weeks
- Milestone-based billing

Please include:
- Links to relevant web apps or dashboards you've built
- Brief note on your experience with API integrations and Python/React projects

Required Skills: Python, React, Web Application, JavaScript''',
        'job_type': 'Hourly',
        'experience_level': 'Expert',
        'budget': 'Hourly: $40.00 - $65.00, Est. time: 1 to 3 months, Not sure'
    },
    {
        'title': 'Python/React/AWS Engineer with Generative AI Expertise',
        'link': 'https://www.upwork.com/jobs/Python-React-AWS-Engineer-with-Generative-Expertise_~021978840129631103856/',
        'description': '''We're looking for a talented full-stack engineer to build a small web application that leverages generative AI to create intelligent, interactive user experiences. This is a compact, well-defined project ideal for a developer who enjoys integrating AI APIs and deploying clean, functional prototypes.

Project Purpose & Key Features:
The goal of this project is to create a simple, interactive web app that showcases how AI can generate useful, creative, or personalized content for users. Key features include:
- A prompt input interface where users can type questions or requests
- A Python backend that calls an AI API
- A React front-end displaying generated text or images dynamically
- User history or session storage
- A clean, responsive UI with mobile support
- Deployed on AWS, with proper environment configuration and key management

Example use cases might include:
- AI-powered content idea generator
- AI summary or writing assistant
- AI image captioning or visualization tool

Scope of Work:
- Develop a minimal React-based web interface (single-page or dashboard layout)
- Implement a Python/FastAPI backend for AI interactions
- Integrate with OpenAI, Anthropic, or Hugging Face APIs
- Store and retrieve basic session data
- Deploy to AWS

Requirements:
- Proficiency in Python/FastAPI and React.js
- Hands-on experience with AI APIs
- Familiarity with AWS services for lightweight deployment
- Understanding of secure key management and environment setup

Required Skills: Next.js, Python, React, TypeScript, Amazon Web Services, AWS Lambda''',
        'job_type': 'Hourly',
        'experience_level': 'Expert',
        'budget': 'Hourly: $70.00 - $85.00, Est. time: Less than 1 month, Less than 30 hrs/week'
    },
    {
        'title': 'Senior Python/TypeScript Engineer for AI Platform Development',
        'link': 'https://www.upwork.com/jobs/Senior-Python-TypeScript-Engineer-for-Platform-Development_~021978528869918562695/',
        'description': '''FlowGenius is a fast-growing AI automation company helping businesses streamline operations with cutting-edge software, workflow automations, and intelligent tools. We're hiring a Senior Full Stack Engineer with strong front-end skills and deep backend automation experience (especially in Python and APIs) to join our elite remote team.

You must be fluent in AI tools and prompt engineering and comfortable building complex systems with limited guidance.

Role Overview:
Position: Senior Full Stack Engineer (AI & Automation)
Type: Full-time, Long-Term

Required Skills:
Front-End: HTML, CSS, JavaScript, React or similar modern framework
Back-End: Advanced Python (automation-heavy work), API development & integration
AI Tools: Strong understanding of tools like OpenAI, HeyGen, Puppeteer, Playwright, Browserbase, Zapier, Make, n8n
Prompt Engineering: You know how to tweak temperature, top_p, and choose the right model for the job
Experience with headless browsers, bot scripting, and process automation
Familiarity with SaaS tools, CRMs, low-code/no-code platforms
Able to build, scale, and optimize complex workflows with AI

Must-Have Qualifications:
- At least 3 years of hands-on experience in both front-end and back-end development
- Demonstrated work with AI models and workflow automation
- Must show proof of past projects (portfolio, GitHub, demos, etc.)
- Comfortable in a fast-paced startup environment
- Strong English communication skills

Tools We Use:
Python, JavaScript, React
OpenAI, Claude, HeyGen, ElevenLabs
Zapier, Make, n8n
Puppeteer, Playwright, Browserbase
Trello, GHL, Slack, Notion

About FlowGenius:
We're an AI-first software company helping businesses automate everything from CRMs to customer support. We move fast, build fast, and break things (intentionally). If you're hungry to work on cutting-edge AI automation projects that make a real-world impact — this is your chance.

How to Apply:
1. Submit your resume/CV
2. Include links to past projects, GitHub, or portfolio
3. Confirm your ability to work 7 AM – 3 PM EST (Mon–Fri)

Application Question(s):
Have you contributed to any open-source projects, or do you have a GitHub profile we can look at?
What is your salary expectations?
Would you describe yourself as Full stack, front end, or back end developer?

Required Skills: Node.js, Python, React, TypeScript, Docker, Git, API''',
        'job_type': 'Hourly',
        'experience_level': 'Expert',
        'budget': 'Hourly: $20.00 - $30.00, Est. time: More than 6 months, 30+ hrs/week'
    },
    {
        'title': 'Part-Time Full-Stack Developer for Financial Analytics Platform',
        'link': 'https://www.upwork.com/jobs/Part-Time-Full-Stack-Developer-for-Financial-Analytics-Platform_~021978124869594683118/',
        'description': '''Part-Time Full-Stack Developer for Financial Analytics Platform (16 hrs/week)

Overview:
We're seeking an experienced full-stack developer to join our team on a part-time basis (2 days/16 hours per week) to help maintain and expand our financial analytics platform. This is a flexible, remote position where you can set your own schedule as long as you deliver consistent weekly hours.

**IMPORTANT:** We are looking for individual US-based developers only. If you are located outside the United States or represent an agency, please do not apply.

Required Technical Skills:

Core Development:
- Ruby on Rails - Strong proficiency in Rails development and best practices
- React - Experience building modern, responsive user interfaces
- PostgreSQL - Advanced SQL skills including query optimization, database design, and performance tuning

Cloud Infrastructure & DevOps:
- AWS Services - Hands-on experience with: EC2, ECS, RDS, Batch, Bedrock

AI/ML Integration:
- RAG Implementation - Experience with Retrieval-Augmented Generation systems
- Python - Ability to develop and maintain Lambda functions
- Claude Code - Familiarity with AI-assisted development tools

Key Responsibilities:

Application Development (Primary):
- Gain comprehensive understanding of our financial analytics platform architecture and business logic
- Design and implement new features based on product requirements
- Enhance and optimize existing functionality
- Identify, troubleshoot, and resolve bugs across the full stack
- Participate in code reviews and maintain high code quality standards

System Administration (Secondary):
- Serve as backup systems administrator during primary admin unavailability
- Monitor system health and respond to critical incidents when needed

Work Arrangement:
- Hours: 16 hours per week (equivalent to 2 full days)
- Schedule: Completely flexible - you choose when to work
- Location: 100% Remote (US-based only)
- Duration: Long-term, ongoing position

To Apply Please include:
- Brief overview of your experience with the required technologies
- Examples of similar platforms or projects you've worked on
- Your availability to start
- Your preferred work schedule/days
- Confirmation you can commit to 16 hours weekly
- Your hourly rate

Required Skills: React, Python, Ruby on Rails, SQL, PostgreSQL, Docker''',
        'job_type': 'Hourly',
        'experience_level': 'Expert',
        'budget': 'Hourly: $50.00 - $105.00, Est. time: More than 6 months, Less than 30 hrs/week'
    },
    {
        'title': 'Full Stack Web Developer for Rapid Prototyping',
        'link': 'https://www.upwork.com/jobs/Full-Stack-Web-Developer-for-Rapid-Prototyping_~021978274737475944068/',
        'description': '''We are seeking a skilled full stack web developer to create rapid prototypes of web applications. These prototypes will be used to showcase ideas to customers and help drive sales.

The ideal candidate should have experience in both front-end and back-end development and be able to work efficiently to deliver high-quality prototypes quickly.

Required Skills: Python, React, Next.js, Google Cloud Platform, JavaScript, HTML5''',
        'job_type': 'Hourly',
        'experience_level': 'Intermediate',
        'budget': 'Hourly: $30.00 - $100.00, Est. time: 1 to 3 months, Less than 30 hrs/week'
    },
]

if __name__ == "__main__":
    print("🎯 REAL UPWORK JOBS - Full Stack React Python")
    print("="*70)
    print(f"\n✅ Found {len(real_jobs)} jobs matching your search")
    print("\n📊 Job Summary:")
    for i, job in enumerate(real_jobs, 1):
        print(f"\n{i}. {job['title']}")
        print(f"   Budget: {job['budget']}")
        print(f"   Level: {job['experience_level']}")

    print("\n" + "="*70)
    print("🚀 Generating cover letters with your automation...")
    print("="*70 + "\n")

    # Save jobs to file
    save_jobs_to_file(real_jobs, './files/upwork_job_listings.txt')

    # Load profile
    profile = read_text_file("./files/profile.md")

    # Create bot
    bot = UpworkAutomationGraph(profile, num_jobs=len(real_jobs))

    # Run automation
    job_listings_str = "\n".join(map(str, real_jobs))

    state = {
        "job_title": "Full Stack React Python (Real Jobs)",
        "scraped_jobs_list": job_listings_str,
        "matches": [],
        "job_description": "",
        "cover_letter": "",
        "num_matches": 0
    }

    print("📊 Classifying jobs with AI...")
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

        print("\n" + "="*70)
        print("✅ DONE! Cover letters saved to: files/cover_letter.txt")
        print("="*70)
        print("\n📋 Next Steps:")
        print("1. Open files/cover_letter.txt")
        print("2. Review each cover letter")
        print("3. Customize the first sentence with specific reference from job")
        print("4. Copy and apply on Upwork!")
        print("\n💡 TIP: Apply to the 'Posted yesterday' jobs first (less competition)")
    else:
        print("\n⚠️  No matching jobs found")
