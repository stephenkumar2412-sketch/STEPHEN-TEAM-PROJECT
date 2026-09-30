import os
import json
import re
import google.generativeai as genai

API_KEY = os.getenv("GEMINI_API_KEY")
if API_KEY:
    genai.configure(api_key=API_KEY)

def _extract_json(text: str):
    text = text.strip()
    text = re.sub(r"^```json\s*", "", text, flags=re.I)
    text = re.sub(r"\s*```$", "", text)
    match = re.search(r"\[.*\]", text, re.S)
    if match:
        text = match.group(0)
    return json.loads(text)

def generate_outline(prompt, character, setting, tone, art_style):
    if not API_KEY:
        raise RuntimeError("GEMINI_API_KEY is not configured.")

    model = genai.GenerativeModel("gemini-1.5-flash")
    instruction = f"""
Create exactly 5 comic panels.

Story idea: {prompt}
Main character: {character}
Setting: {setting}
Tone: {tone}
Art style: {art_style}

Return ONLY valid JSON as an array of 5 objects.
Each object must contain:
panel_number, title, scene_description, image_prompt.

Make the story coherent from panel 1 to panel 5.
"""
    response = model.generate_content(instruction)
    return _extract_json(response.text)
