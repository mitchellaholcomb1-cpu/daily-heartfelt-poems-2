
import os
from datetime import datetime, timezone
from pathlib import Path
from google import genai

# Connect to Gemini using your GitHub secret
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

# Get today's date
today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

# Ask AI to write a heartfelt poem
prompt = """
Write one original, heartfelt poem for someone deeply special.

Requirements:
- Make it sincere, warm, and emotionally meaningful.
- Express affection, appreciation, and encouragement.
- Use 8 to 12 lines.
- Make it sound personal and genuine.
- Do not include a title, explanation, or quotation marks.
- Write a different poem each day.
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

poem = response.text.strip()

# Save the poem in a dated file
folder = Path("poems")
folder.mkdir(exist_ok=True)

file_path = folder / f"{today}.txt"
file_path.write_text(poem + "\n", encoding="utf-8")

print(f"Today's poem saved to {file_path}")
print(poem)
