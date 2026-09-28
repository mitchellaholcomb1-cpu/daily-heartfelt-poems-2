import os
from datetime import datetime, timezone
from pathlib import Path
from google import genai

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

prompt = """
Write one original, heartfelt poem for someone deeply special.

Requirements:
- Make it sincere, warm, and emotionally meaningful.
- Express affection, appreciation, and encouragement.
- Use 8 to 12 lines.
- Make it sound personal and genuine.
- Do not include a title or explanation.
"""

response = client.models.generate_content(
    model="gemini-3.1-flash",
    contents=prompt
)

poem = response.text.strip()

folder = Path("poems")
folder.mkdir(exist_ok=True)

file_path = folder / f"{today}.txt"
file_path.write_text(poem + "\n", encoding="utf-8")

print(f"Today's poem saved to {file_path}")
print(poem)
