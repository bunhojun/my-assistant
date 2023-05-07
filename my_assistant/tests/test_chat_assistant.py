from ..chat_assistant import ChatAssistant


def test_chat_assistant():
    """Test chat assistant"""
    assistant = ChatAssistant()
    input_text = "あなたの名前はなんですか"
    result = assistant.chat(input_text)
    assert "ブンブン" in result
