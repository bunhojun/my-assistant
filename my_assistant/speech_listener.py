import sounddevice as sd
import speech_recognition as sr
import numpy as np


class SpeechListener:
    def __init__(self, sample_rate=16000, chunk_duration=8):
        self.sample_rate = sample_rate
        self.chunk_duration = chunk_duration
        self.chunk_samples = chunk_duration * sample_rate
        self.r = sr.Recognizer()

    def on_record(self, in_data, callback):
        audio_data = np.frombuffer(in_data, dtype=np.int16)
        source = sr.AudioData(audio_data.tobytes(), self.sample_rate, 2)
        try:
            text: str = self.r.recognize_google(source, language='ja-JP')
            callback(text)
        except sr.UnknownValueError:
            pass

    def use_stream(self, callback):
        return sd.InputStream(
            samplerate=self.sample_rate,
            channels=1,
            dtype=np.int16,
            blocksize=self.chunk_samples,
            callback=lambda in_data, _a, _b, _c: self.on_record(
                in_data,
                callback,
            ),
        )

    def record(self, duration):
        sd.sleep(duration * 1000)
