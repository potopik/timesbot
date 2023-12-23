import telebot
import datetime
from settings import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Привет! Я могу показать текущее время, просто напиши /time')

@bot.message_handler(commands=['time'])
def send_time(message):
    now = datetime.datetime.now()
    time_now = now.strftime('%d-%m-%Y %H:%M:%S')
    bot.reply_to(message, f"Текущее время: {time_now}")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Вот список доступных команд:\n/start - начало работы\n/time - узнать текущее время\n/help - помощь")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Извините, я не понимаю эту команду. Напишите /help для получения списка команд.")

if __name__ == "__main__":
    print('Bot is running')
    bot.infinity_polling()