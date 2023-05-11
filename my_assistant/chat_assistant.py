from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain import LLMChain


class ChatAssistant:
    def __init__(self):
        self.chain = LLMChain(
            llm=ChatOpenAI(),
            prompt=ChatPromptTemplate.from_messages([
                SystemMessagePromptTemplate.from_template(
                    "あなたの名前はブンブンです。あなたは返事を100字以内で返します。"
                ),
                MessagesPlaceholder(variable_name="history"),
                HumanMessagePromptTemplate.from_template("{input}")
            ]),
            memory=ConversationBufferMemory(return_messages=True),
        )

    def chat(self, text: str):
        print('質問: ', text)
        result = self.chain.run(text)
        print('答え: ', result)
        return result


"""Example usage"""
if __name__ == "__main__":
    assistant = ChatAssistant()
    input_text = "おはようございます！"  # Replace with any desired text
    assistant.chat(input_text)
