from chat_assistant import ChatAssistant
from text_to_speech_player import TextToSpeechPlayer
from speech_listener import listen_for_audio
from utils import is_keyword
from dotenv import load_dotenv

load_dotenv()


def main():

    assistant = ChatAssistant()
    ttsp = TextToSpeechPlayer('ja')

    print("Listening...")
    while True:
        text = listen_for_audio(listen_seconds=9)
        if text and is_keyword(text):
            print('keyword detected')
            ttsp.play_text('はい')
            result = assistant.chat(text)
            ttsp.play_text(result)
        elif text:
            print('text ', text)


if __name__ == "__main__":
    main()
