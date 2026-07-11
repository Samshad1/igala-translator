# Igala Translate Backend Server
# Keeps the Groq API key hidden from the public website
import os
import csv
from flask import Flask, request, jsonify
from flask_cors import CORS
from groq import Groq
app = Flask(__name__)
CORS(app)  # Allows your website to talk to this server
# Load the dictionary from the CSV
def load_dictionary():
    words = {}
    with open("igala_words.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            english = row["english"].lower().strip()
            igala = row["igala_primary"].strip()
            if english and igala:
                words[english] = igala
    return words
dictionary = load_dictionary()

IGALA_ALPHABET_REFERENCE = """
IGALA ALPHABET REFERENCE (verified by native speaker, formally studied in school):

Vowels (7 base vowels): a, e, ẹ, i, o, ọ, u
- Tone marks (e.g. ọ́, ọ̀, é, è) are NOT separate letters. They are added on top of the
  7 base vowels specifically to distinguish homographs — words that are spelled the
  same but mean different things and are pronounced with a different tone.
  Example: "olu" vs "ólù" — same spelling without tone marks, different words.
  Always include the correct tone mark when it distinguishes meaning.

Consonants: b, d, f, g, h, j, k, l, m, n, p, r, t, w, y

Combined/special letters unique to Igala (digraphs): ch, gb, gw, kp, kw, ng, nm, nw, ny, un
- These represent single distinct sounds in Igala with no equivalent single English letter.

Full alphabet order:
a, b, ch, d, e, ẹ, f, g, gb, gw, h, i, j, k, kp, kw, l, m, n, ng, nm, nw, ny, o, ọ, p, r, t, u, w, y
"""

@app.route("/translate", methods=["POST"])
def translate():
    data = request.get_json()
    text = data.get("text", "").strip()
    direction = data.get("direction", "en_to_ig")
    if not text:
        return jsonify({"error": "No text provided"}), 400
    # Build dictionary reference for the AI
    dict_reference = "\n".join([f"{en} = {ig}" for en, ig in dictionary.items()])
    direction_instruction = (
        "Translate the following English text to Igala."
        if direction == "en_to_ig"
        else "Translate the following Igala text to English."
    )
    system_prompt = f"""You are an expert Igala language translator. Igala is spoken in Kogi State, Nigeria.
Use this verified dictionary from native Igala speakers as your primary reference:
{dict_reference}

{IGALA_ALPHABET_REFERENCE}

Key grammar rules:
- The full/formal form of "I" is "omi na". In everyday spoken sentences, "na" alone is
  the common short form and comes FIRST in the sentence, before the verb
  (e.g. "I want to eat" -> "Na tene jẹ ujẹnwu", NOT "Tene na jẹ ujẹnwu").
- Polite requests can start with "Agba" (please) before the sentence, e.g.
  "Agba, na tene jẹ ujẹnwu" or end with a softener like "kocho".
- Words in Igala connect and merge naturally — construct a flowing sentence, not word-by-word.
- Always use the correct Igala tone marks as described in the alphabet reference above,
  especially where a word would otherwise be a homograph with a different meaning.
- Return ONLY the translation, nothing else."""
    try:
        client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"{direction_instruction}\n\nText: {text}"}
            ],
            max_tokens=500,
            temperature=0.3
        )
        translation = response.choices[0].message.content.strip()
        return jsonify({"translation": translation, "mode": "ai"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "words": len(dictionary)})
if __name__ == "__main__":
     import os
     port = int(os.environ.get("PORT", 5000))
     app.run(host="0.0.0.0", port=port)
