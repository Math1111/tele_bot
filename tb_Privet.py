import telebot

# Замените 'YOUR_BOT_TOKEN' на токен вашего бота
TOKEN = '7804854429:AAGTDtTwcwKWWJnT2SyCecmU00bBl4RZHbo'
bot = telebot.TeleBot(TOKEN)

# Обработчик всех текстовых сообщений
@bot.message_handler(func=lambda message: True)
def echo_all(message):
   bot.reply_to(message, "Привет! Как дела?")

# Запуск бота
bot.polling(none_stop=True)