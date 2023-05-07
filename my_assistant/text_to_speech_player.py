from gtts import gTTS
import io
from pydub import AudioSegment
from pydub.playback import play


class TextToSpeechPlayer:
    def __init__(self, language="en"):
        self.language = language

    def play_text(self, text, playback_speed=1.3):
        tts = gTTS(text, lang=self.language)
        with io.BytesIO() as f:
            tts.write_to_fp(f)
            f.seek(0)
            audio = AudioSegment.from_file(f, format="mp3")
            audio = audio.speedup(playback_speed)
            play(audio)


"""Example usage"""
if __name__ == "__main__":
    tts = TextToSpeechPlayer()
    tts.play_text("Hello, how are you?")
