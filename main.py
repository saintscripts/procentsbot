import telebot

import random

TOKEN = "токен из @botfather"

bot = telebot.TeleBot(TOKEN)

gay = str(random.randint(0,100))

dick = str(random.randint(0,1000))

@bot.message_handler(commands=['start'])

def welcome(message):

	bot.send_message(message.chat.id, "Привет, я определяю что-то) К примеру на сколько ты гей) \nСписок команд:\n/gay - определю на сколько ты гей, например сейчас ты гей на " + str(random.randint(0,100)) + "%\n/dick - определит размер твоего лысого друга, например сейчас размер твоего друга " + dick + "см\n/gays - опрелелит насколько ты истиный фанат моргенштерна и славы мерлоу и влада а4\nРазработчик: @saintfukk2")	

@bot.message_handler(content_types=["new_chat_members"])

def handler_new_member(message):

	bot.send_message(message.chat.id, "Привет, я определяю что-то) К примеру на сколько ты гей) \nСписок команд:\n/gay - определю на сколько ты гей, например сейчас ты гей на " + str(random.randint(0,1000)) + "%\n/dick - определит размер твоего лысого друга, например сейчас размер твоего друга " + dick + "см\n/gays - опрелелит насколько ты истиный фанат моргенштерна и славы мерлоу и влада а4\nРазработчик: @saintfukk2")

	

@bot.message_handler(commands=['gay'])

def gayc(message):

	bot.send_message(message.chat.id, "Ты гей на " + str(random.randint(0,100)) + "%")

	

@bot.message_handler(commands=['dick'])

def dickc(message):

	bot.send_message(message.chat.id, "Размер твоего члена: " + str(random.randint(0,1000)) + " сантиметров")

	

@bot.message_handler(commands=['gays'])

def dickc(message):

	bot.send_message(message.chat.id, "Ты истинный фанат MORGENSHTERN'а, Влада А4 и Славы Мерлоу на " + str(random.randint(100, 200)) + "%")

	

bot.polling()
