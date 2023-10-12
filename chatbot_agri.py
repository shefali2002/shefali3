from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


agri_bot = ChatBot('AgricultureBot')


trainer = ChatterBotCorpusTrainer(agri_bot)


trainer.train("chatterbot.corpus.indian.agri")


response = agri_bot.get_response("What are some common crops grown in India?")

print(response)
