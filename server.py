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

Key grammar rules:
- "I" in Igala: mostly "na" in sentences, full form is "omi na"
- Words in Igala connect and merge naturally, construct flowing sentences
- Always use proper Igala tone marks
- Return ONLY the translation, nothing else"""

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