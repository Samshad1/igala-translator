# English - Igala Translator
# Original code by: Sani Samuel Ojochegbe
# Igala language contributor: Ann (and her mum)
import csv

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

def translate(phrase):
    translation = ""
    words = phrase.split()

    for word in words:
        lower_word = word.lower()
        if lower_word in translation_rules:
            translated_word = translation_rules[lower_word]
            if isinstance(translated_word, list):
                translated_word = translated_word[0]
            if word.islower():
                translated_word = translated_word.lower()
            elif word.isupper():
                translated_word = translated_word.upper()
            elif word.istitle():
                translated_word = translated_word.capitalize()
            translation += translated_word + " "
        else:
            translation += word + " "

    return translation.strip()

print("=" * 40)
print("  English - Igala Translator")
print("  Type 'quit' to exit")
print("=" * 40)

while True:
    phrase = input("\nEnter a phrase: ")
    if phrase.lower() == "quit":
        print("Goodbye! / Chẹ́gbatugba!")
        break
    result = translate(phrase)
    print(f"Igala: {result}")