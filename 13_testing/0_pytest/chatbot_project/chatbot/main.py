from chatbot.bot import Chatbot
from chatbot.helper import clean_message

bot = Chatbot("ChatGPT-Bot")


if __name__ == "__main__":
    print(bot.greet())

    msg = input("Nachricht: ")
    msg_clean = clean_message(msg)
    bot.remember(msg_clean)
    antwort = bot.ask_api(msg_clean)
    print(antwort)
