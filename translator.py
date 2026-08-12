from deep_translator import GoogleTranslator
from langdetect import detect


LANGUAGES = {
    "English": "en",
    "Urdu": "ur",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Italian": "it",
    "Hindi": "hi",
    "Arabic": "ar",
    "Chinese": "zh-CN",
    "Japanese": "ja",
    "Korean": "ko",
    "Russian": "ru",
    "Turkish": "tr",
    "Portuguese": "pt"
}


REVERSE_LANGUAGES = {
    "en": "English",
    "ur": "Urdu",
    "fr": "French",
    "de": "German",
    "es": "Spanish",
    "it": "Italian",
    "hi": "Hindi",
    "ar": "Arabic",
    "zh-cn": "Chinese",
    "zh-tw": "Chinese",
    "ja": "Japanese",
    "ko": "Korean",
    "ru": "Russian",
    "tr": "Turkish",
    "pt": "Portuguese"
}


def detect_language(text):

    text = text.strip()

    if len(text) < 3:
        return "English"

    try:

        detected_code = detect(text)

        return REVERSE_LANGUAGES.get(
            detected_code,
            "English"
        )

    except Exception:

        return "English"


def translate_text(text, source_language, target_language):

    text = text.strip()

    if text == "":
        return ""

    if source_language not in LANGUAGES:
        source_language = "English"

    if target_language not in LANGUAGES:
        target_language = "English"

    if source_language == target_language:
        return text

    try:

        translator = GoogleTranslator(
            source=LANGUAGES[source_language],
            target=LANGUAGES[target_language]
        )

        translated = translator.translate(text)

        return translated

    except Exception as e:

        return f"Error : {e}"