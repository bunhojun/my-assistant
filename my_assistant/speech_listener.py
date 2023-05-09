import sounddevice
import speech_recognition as sr

# Due to an installation issue with pyaudio, use sounddevice instead
sounddevice
r = sr.Recognizer()


def listen_for_audio(
        listen_seconds: int = 10,
        language: str = 'ja-JP') -> str | None:
    """Listens for audio from the microphone

    Returns:
        str: The recognized speech from the audio
    """
    try:
        with sr.Microphone() as audio_source:
            r.adjust_for_ambient_noise(audio_source, duration=0.2)
            audio2 = r.listen(
                audio_source, timeout=3,
                phrase_time_limit=listen_seconds,
            )
            text = r.recognize_google(
                audio2,
                language=language,
            )
            return text

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        print("unknown error occurred")
    except sr.WaitTimeoutError:
        print("No voice detected")
