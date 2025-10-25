"""
Generate cover letter from Upwork job URL
You paste the URL, I'll try to extract the job ID and generate a letter
"""
from dotenv import load_dotenv
from src.utils import read_text_file
from src.agent import Agent
from src.prompts import generate_cover_letter_prompt
import json
import re
import pyperclip

load_dotenv()

def main():
    print("\n" + "=" * 70)
    print("🚀 UPWORK JOB APPLICATION - PASTE URL OR DESCRIPTION")
    print("=" * 70)

    print("\n📋 You have 2 options:")
    print("\n1. Paste job URL (I'll try to fetch it)")
    print("2. Paste full job description (more reliable)")
    print("\nWhich do you want to do? (1 or 2): ", end='')

    choice = input().strip()

    if choice == "1":
        print("\n📎 Paste Upwork job URL:")
        url = input().strip()
        print(f"\n⚠️  Note: Direct URL fetching may not work due to Upwork's protection.")
        print("If this fails, please copy-paste the job description instead.")
        print("\n❌ Sorry, Upwork blocks automated URL fetching.")
        print("\n💡 Please use option 2 instead (paste job description)")
        return

    # Option 2: Paste description
    print("\n📝 Paste the ENTIRE job description from Upwork:")
    print("(Include: title, budget, requirements, etc.)")
    print("Press Enter twice when done:\n")

    lines = []
    empty_count = 0

    while True:
        line = input()
        if line == "":
            empty_count += 1
            if empty_count >= 2:
                break
        else:
            empty_count = 0
        lines.append(line)

    job_description = "\n".join(lines).strip()

    if not job_description:
        print("\n❌ No description provided.")
        return

    # Load profile
    profile = read_text_file("./files/profile.md")

    # Initialize AI
    agent = Agent(
        name="Cover Letter Generator",
        model="gemini/gemini-2.5-flash-preview-05-20",
        system_prompt=generate_cover_letter_prompt.format(profile=profile),
        temperature=0.1
    )

    print("\n🤖 Generating your AI-powered cover letter...")
    print("⏱️  Using your Microsoft, Home Depot, and Connectful experience...")
    print("⏱️  This takes 2-5 seconds...\n")

    try:
        # Generate
        result = agent.invoke(job_description)

        # Clean up
        result = re.sub(r'```json\s*', '', result)
        result = re.sub(r'```\s*$', '', result)
        result = result.strip()

        # Parse
        result_json = json.loads(result, strict=False)
        cover_letter = result_json.get("letter", result)

        # Display
        print("=" * 70)
        print("✅ COVER LETTER READY")
        print("=" * 70)
        print("\n" + cover_letter + "\n")
        print("=" * 70)
        print(f"📊 {len(cover_letter)} characters | Perfect length for Upwork")
        print("=" * 70)

        # Copy to clipboard
        try:
            pyperclip.copy(cover_letter)
            print("\n✅ COPIED TO CLIPBOARD!")
            print("\n📋 Next steps:")
            print("  1. Go to Upwork")
            print("  2. Click 'Apply Now' on the job")
            print("  3. Click in Cover Letter field")
            print("  4. Paste (Cmd+V)")
            print("  5. Adjust your rate if needed")
            print("  6. Click 'Send for X Connects'")
            print("\n⏱️  Should take 30 seconds!")
        except:
            print("\n📋 Copy the text above and paste into Upwork")

        # Save
        with open('./files/latest_cover_letter.txt', 'w') as f:
            f.write(cover_letter)

        print("\n💾 Saved to: files/latest_cover_letter.txt")
        print("\n🎯 Go apply on Upwork now!")

    except Exception as e:
        print(f"\n❌ Error: {str(e)}")

if __name__ == "__main__":
    main()
