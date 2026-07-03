# English - Igala Translator (AI-Powered)
# Original code by: Sani Samuel Ojochegbe
# Igala language contributor: Ann (and her mum)
# Built with AI assistance

import os
from google import genai

api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise EnvironmentError("GEMINI_API_KEY secret is not set. Add it via Replit Secrets.")
client = genai.Client(api_key=api_key)

# Verified Igala dictionary by Ann
translation_rules = {
    "hello": "agba",
    "good morning": "wola odudu",
    "good afternoon": "ọlọ́rọka",
    "good evening": "ọlá'nẹ",
    "good night": "wola ane",
    "welcome": "ọlalẹ",
    "thank you": "wolu'kọlọ",
    "please": "awa",
    "sorry": "nago",
    "yes": "i-i",
    "no": "ọda-aa",
    "goodbye": "chẹ́gbatugba",
    "mother": "iye",
    "father": "ata",
    "child": "ọma",
    "brother": "ọmaye ọnẹkẹle",
    "sister": "ọmaye ọnọbule",
    "friend": "onuku",
    "man": "ọnẹkẹle",
    "woman": "ọnọbule",
    "king": "ọnu",
    "person": "onẹ",
    "eat": "jẹ",
    "drink": "mo",
    "sleep": "ólu",
    "wake up": "j'ólu",
    "go": "lo",
    "come": "wa",
    "run": "rule",
    "sit": "gwane",
    "stand": "dago",
    "want": "tenẹ",
    "love": "fẹdo",
    "see": "li",
    "give": "du",
    "take": "gbà",
    "buy": "la",
    "sell": "ta",
    "work": "ukọlọ",
    "pray": "aduwa",
    "cook": "yẹnwu",
    "wash": "gwe",
    "food": "ujẹnwu",
    "water": "omi",
    "house": "unyi",
    "road": "ọna",
    "money": "ọ́kọ́",
    "book": "otakada",
    "clothes": "ukpo",
    "fire": "una",
    "land": "ane",
    "god": "ọjọ",
    "one": "ényẹ́",
    "two": "èjì",
    "three": "ẹ̀ta",
    "four": "ẹ̀lẹ̀",
    "five": "ẹ̀lú",
    "today": "eñini",
    "tomorrow": "ọna",
    "yesterday": "ọnalẹ",
    "morning": "òdùdu",
    "night": "anẹ",
    "canoe": "ọkó èjomi",
    "husband": "òkọ",
    "millipede": "ọkọ",
}

def translate_with_ai(phrase):
    # Build the dictionary as a reference for the AI
    dictionary_reference = "\n".join(
        [f"{eng} = {iga}" for eng, iga in translation_rules.items()]
    )

    prompt = f"""You are an expert Igala language translator. 
Igala is spoken in Kogi State, Nigeria.

Use this verified Igala dictionary as your reference:
{dictionary_reference}

Translate this English text to Igala: "{phrase}"

Rules:
- Use the dictionary words above as much as possible
- For words not in the dictionary, use your knowledge of Igala
- Return ONLY the Igala translation, nothing else
- Preserve proper Igala tone marks"""

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
    return response.text.strip()

print("=" * 40)
print("  English to Igala Translator (AI)")
print("  Contributor: Ann")
print("=" * 40)

while True:
    phrase = input("\nEnter English phrase (or 'quit' to exit): ")
    if phrase.lower() == "quit":
        print("Goodbye! / Chẹ́gbatugba!")
        break
    result = translate_with_ai(phrase)
    print(f"Igala: {result}")