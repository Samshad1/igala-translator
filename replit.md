# English–Igala Translator

A Python project that translates English words and phrases into Igala, a language spoken in Kogi State, Nigeria.

**Original code:** Sani Samuel Ojochegbe  
**Igala language contributor:** Ann (and her mum)

## Files

| File | Description |
|------|-------------|
| `igala_translator.py` | Basic translator with hardcoded word rules — the main runnable script |
| `igala_translator_ai.py` | AI-powered version using Google Gemini |
| `igala_words.csv` | Verified Igala dictionary (CSV format) |

## How to run

The **basic translator** runs automatically via the configured workflow:

```
python igala_translator.py
```

Type a phrase in the console and press Enter. Type `quit` to exit.

## AI-powered version

To run the Gemini-powered translator:

```
python igala_translator_ai.py
```

**Requires:** `GEMINI_API_KEY` set as a Replit Secret.

## User preferences

- Keep the project's existing structure and stack.
