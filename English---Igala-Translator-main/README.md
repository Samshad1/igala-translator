# English---Igala-Translator
This is the code for an English to Igala Translator on Python. 

def translate(phrase):
    # Translation rules for English to Igala.
    translation_rules = {
        "to sew": "ga",
        "stitch": "ga",
        "greet": "gwa",
        "to run": "ra",
        "to escape": "ra",
        "market": "aja",
        "dog": "abia",
        "to read": "gba",
        "weldone": ["agba", "awa"],
        "to stop": "wee",
        "halt": "wee",
        "to do": "che",
        "make to": "che",
        "invent": "che",
        "who": "ene",
        "you": "uwe",
        "how": "abu",
        "are": "e",
        "has": "mu",
        "my": "mi",
        "have": "f",
        "i": "u",
        "speak": "ka",
        "say": "ka",
        "to speak": "ka",
        "know": "ma",
        "build": "ko",
        "built": "ko",
        "created": "ko",
        "write": "ako",
        "good morning": "wola odudu",
        "good night": "wola ane",
        "hear": "gbo",
        "listen": "gbo",
        "words": "ola",
        "python": "elee",
        "translate": "gbolaje",
        "translator": "agbolaje",
        "inside": "efi",
        "english": "enefu",
        "do": "na",
        "in":"lali",
        "igalaa": "igala"
    }

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


print(translate(input("Enter a phrase: ")))
