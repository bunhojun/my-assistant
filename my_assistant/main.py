from chat_assistant import ChatAssistant
from text_to_speech_player import TextToSpeechPlayer
from speech_listener import listen_for_audio
from utils import is_keyword
from dotenv import load_dotenv

load_dotenv()


def main():
    is_active = False

    assistant = ChatAssistant()
    ttsp = TextToSpeechPlayer('ja')

    print("Listening...")
    while True:
        if not is_active:
            text = listen_for_audio(listen_seconds=2)
            if not text or not is_keyword(text):
                continue
            print('keyword detected')
            ttsp.play_text('はい')
            is_active = True
        else:
            text = listen_for_audio(listen_seconds=10)
            if not text:
                continue
            result = assistant.chat(text)
            ttsp.play_text(result)
            is_active = False


if __name__ == "__main__":
    main()
