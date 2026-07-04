# English - Igala Translator (AI-Powered)
# Original code by: Sani Samuel Ojochegbe
# Igala language contributor: Ann (and her mum)
# Built with AI assistance

import os
import csv
from groq import Groq

api_key = os.environ.get("GROQ_API_KEY")
if not api_key:
    raise EnvironmentError("GROQ_API_KEY secret is not set. Add it via Replit Secrets.")
client = Groq(api_key=api_key)

def load_words_from_csv(filename):
    translation_rules = {}
    with open(filename, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            english = row["english"].lower().strip()
            igala = row["igala_primary"].strip()
            if english and igala:
                translation_rules[english] = igala
    return translation_rules

translation_rules = load_words_from_csv("igala_words.csv")

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
1. The word 'I' in Igala has multiple forms depending on context: 'omi' (I am going/movement), 'na' (I want/action), 'u' (I love/feelings), 'un' (I said/speech). Choose the correct one based on the sentence.
2. Words in Igala often connect and merge together — don't just swap word by word, construct a natural flowing Igala sentence.
3. Always use the verified dictionary words provided above as your primary reference.
4. For words not in the dictionary, make your best guess based on Igala language patterns.
5. Return ONLY the Igala translation, nothing else."""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

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
