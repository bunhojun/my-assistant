from chat_assistant import ChatAssistant
from text_to_speech_player import TextToSpeechPlayer
from speech_listener import SpeechListener
from utils import is_keyword
from dotenv import load_dotenv

load_dotenv()

initial_duration = 4


def main():
    chunk_duration = initial_duration
    is_active = False

    sl = SpeechListener(chunk_duration=chunk_duration)
    assistant = ChatAssistant()
    ttsp = TextToSpeechPlayer('ja')

    def callback(text: str):
        nonlocal is_active, chunk_duration
        if not is_active:
            print('not active: ', text)
        if is_active:
            is_active = False
            result = assistant.chat(text)
            ttsp.play_text(result)
            chunk_duration = initial_duration
            return
        if is_keyword(text):
            ttsp.play_text('はい')
            chunk_duration = 10
            is_active = True

    with sl.use_stream(callback):
        print("Listening...")
        while True:
            sl.listen(chunk_duration)


if __name__ == "__main__":
    main()
