"""
Quick Upwork Application - Simple copy-paste method
No server, no bookmarklet, just paste job description and get cover letter
"""
from dotenv import load_dotenv
from src.utils import read_text_file
from src.agent import Agent
from src.prompts import generate_cover_letter_prompt
import json
import re
import pyperclip  # Will copy to clipboard automatically

load_dotenv()

def main():
    print("\n" + "=" * 70)
    print("🚀 QUICK UPWORK APPLICATION")
    print("=" * 70)

    # Load profile
    profile = read_text_file("./files/profile.md")

    # Initialize AI agent
    agent = Agent(
        name="Cover Letter Generator",
        model="gemini/gemini-2.5-flash-preview-05-20",
        system_prompt=generate_cover_letter_prompt.format(profile=profile),
        temperature=0.1
    )

    print("\n📋 Instructions:")
    print("1. Go to Upwork job page")
    print("2. Copy the ENTIRE job description")
    print("3. Paste it below")
    print("4. Press Enter twice when done")
    print("\n" + "-" * 70)

    # Get job description
    print("\n📝 Paste job description (press Enter twice when done):\n")
    lines = []
    while True:
        line = input()
        if line == "" and len(lines) > 0 and lines[-1] == "":
            break
        lines.append(line)

    job_description = "\n".join(lines).strip()

    if not job_description:
        print("\n❌ No job description provided. Exiting.")
        return

    print("\n🤖 Generating AI cover letter...")
    print("⏱️  This takes 2-5 seconds...\n")

    # Generate cover letter
    try:
        cover_letter_result = agent.invoke(job_description)

        # Clean up response
        cover_letter_result = re.sub(r'```json\s*', '', cover_letter_result)
        cover_letter_result = re.sub(r'```\s*$', '', cover_letter_result)
        cover_letter_result = cover_letter_result.strip()

        # Parse JSON
        result_json = json.loads(cover_letter_result, strict=False)
        cover_letter = result_json.get("letter", cover_letter_result)

        print("=" * 70)
        print("✅ COVER LETTER GENERATED")
        print("=" * 70)
        print("\n" + cover_letter + "\n")
        print("=" * 70)
        print(f"📊 Length: {len(cover_letter)} characters")
        print("=" * 70)

        # Try to copy to clipboard
        try:
            pyperclip.copy(cover_letter)
            print("\n✅ Copied to clipboard!")
            print("📋 Just paste (Cmd+V) into Upwork!")
        except:
            print("\n💡 Copy the text above and paste into Upwork")

        # Save to file
        with open('./files/latest_cover_letter.txt', 'w') as f:
            f.write(cover_letter)

        print("\n💾 Also saved to: files/latest_cover_letter.txt")
        print("\n🚀 Go paste it into Upwork and click Send!")

    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        print("Try again or check your internet connection")

if __name__ == "__main__":
    main()
