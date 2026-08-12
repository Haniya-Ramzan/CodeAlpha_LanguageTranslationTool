import pyttsx3


def speak_text(text):

    try:

        engine = pyttsx3.init("sapi5")


        voices = engine.getProperty("voices")


        engine.setProperty(
            "rate",
            150
        )


        engine.setProperty(
            "volume",
            1.0
        )


        engine.say(text)

        engine.runAndWait()

        engine.stop()


    except Exception as e:

        print(
            "Speech Error:",
            e
        )