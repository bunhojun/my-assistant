import sounddevice as sd
import speech_recognition as sr
import numpy as np
from chat_assistant import ChatAssistant
from text_to_speech_player import TextToSpeechPlayer


def is_keyword(text: str):
    return 'OK' in text and ('ブンブン' in text or 'ぶんぶん' in text)


initial_duration = 8


def main():
    sample_rate = 16000  # 16 kHz
    chunk_duration = initial_duration
    chunk_samples = chunk_duration * sample_rate
    is_active = False
    is_responding = False

    r = sr.Recognizer()
    assistant = ChatAssistant()
    ttsp = TextToSpeechPlayer('ja')

    def callback(in_data, _a, _b, _c):
        nonlocal is_active, chunk_duration, is_responding
        audio_data = np.frombuffer(in_data, dtype=np.int16)
        source = sr.AudioData(audio_data.tobytes(), sample_rate, 2)
        try:
            text: str = r.recognize_google(source, language='ja-JP')
            if not is_active:
                print('not active: ', text)
            if 'ありがとう' in text:
                is_active = False
                is_responding = True
                result = assistant.chat(text)
                ttsp.play_text(result)
                is_responding = False
                chunk_duration = initial_duration
                return
            if not is_responding and (is_active or is_keyword(text)):
                is_active = True
                chunk_duration = 18
                is_responding = True
                result = assistant.chat(text)
                ttsp.play_text(result)
                is_responding = False

        except sr.UnknownValueError:
            pass

    with sd.InputStream(
        samplerate=sample_rate,
        channels=1,
        dtype=np.int16,
        blocksize=chunk_samples,
        callback=callback,
    ):
        print("Listening...")
        while True:
            sd.sleep(chunk_duration * 1000)


if __name__ == "__main__":
    main()
