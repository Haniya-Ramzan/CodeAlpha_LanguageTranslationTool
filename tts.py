from gtts import gTTS
import os


LANGUAGE_CODES = {

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



def generate_speech(text, language, filename):

    try:

        code = LANGUAGE_CODES.get(
            language,
            "en"
        )


        speech = gTTS(
            text=text,
            lang=code,
            slow=False
        )


        speech.save(filename)


        os.startfile(filename)


        return True


    except Exception as e:

        print("Speech Error:", e)

        return False



def speak_multilingual(text, language):

    return generate_speech(
        text,
        language,
        "translation.mp3"
    )