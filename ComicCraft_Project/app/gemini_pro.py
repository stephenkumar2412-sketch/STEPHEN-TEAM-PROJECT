import os
import google.generativeai as genai

API_KEY = os.getenv("GEMINI_API_KEY")
if API_KEY:
    genai.configure(api_key=API_KEY)

def generate_story(outline, character, tone):
    if not API_KEY:
        raise RuntimeError("GEMINI_API_KEY is not configured.")

    model = genai.GenerativeModel("gemini-1.5-pro")
    prompt = f"""
Write the narration and dialogue for this 5-panel comic.

Main character: {character}
Tone: {tone}

Panel outline:
{outline}

For every panel return:
Panel number
Caption
Narration
Dialogue

Keep the story concise and comic-book friendly.
"""
    response = model.generate_content(prompt)
    return response.text
