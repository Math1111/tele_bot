import telebot
from datetime import datetime
import pytz

# Замените 'YOUR_API_TOKEN' на токен вашего бота
API_TOKEN = '7784451071:AAHdipIeYPc8PU0PsVy8gg8_K2E6aNJhawo'
bot = telebot.TeleBot(API_TOKEN)

# Словарь с часовыми поясами для российских городов
timezones = {
    "москва": "Europe/Moscow",
    "санкт-петербург": "Europe/Moscow",
    "новосибирск": "Asia/Novosibirsk",
    "екатеринбург": "Asia/Yekaterinburg",
    "нижний новгород": "Europe/Moscow",
    "казань": "Europe/Moscow",
    "челябинск": "Asia/Yekaterinburg",
    "омск": "Asia/Omsk",
    "ростов-на-дону": "Europe/Moscow",
    "уфа": "Europe/Moscow",
    "красноярск": "Asia/Krasnoyarsk",
    "пермь": "Asia/Yekaterinburg",
    "воронеж": "Europe/Moscow",
    "волгоград": "Europe/Moscow",
    "краснодар": "Europe/Moscow",
    "самара": "Europe/Samara",
    "саратов": "Europe/Saratov",
    "тюмень": "Asia/Yekaterinburg",
    "тольятти": "Europe/Samara",
    "ижевск": "Europe/Samara",
    "барнаул": "Asia/Novosibirsk",
    "иркутск": "Asia/Irkutsk",
    "хабаровск": "Asia/Vladivostok",
    "ярославль": "Europe/Moscow",
    "кострома": "Europe/Moscow",
    "владивосток": "Asia/Vladivostok",
    "махачкала": "Europe/Moscow",
    "томск": "Asia/Novosibirsk",
    "оренбург": "Asia/Yekaterinburg",
    "кемерово": "Asia/Krasnoyarsk",
    "новокузнецк": "Asia/Krasnoyarsk",
    "рязань": "Europe/Moscow",
    "астрахань": "Europe/Volgograd",
    "набережные челны": "Europe/Moscow",
    "пенза": "Europe/Moscow",
    "липецк": "Europe/Moscow",
    "киров": "Europe/Moscow",
    "чебоксары": "Europe/Moscow",
    "балашиха": "Europe/Moscow",
    "калининград": "Europe/Kaliningrad",
    "тула": "Europe/Moscow",
    "курск": "Europe/Moscow",
    "севастополь": "Europe/Simferopol",
    "сочи": "Europe/Moscow",
    "ставрополь": "Europe/Moscow",
    "улан-удэ": "Asia/Irkutsk",
    "тверь": "Europe/Moscow",
}
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Напиши название города в России, и я скажу тебе, какое в нём сейчас время.")

@bot.message_handler(func=lambda message: True)
def get_time(message):
    city = message.text.lower()
    if city in timezones:
        timezone = pytz.timezone(timezones[city])
        current_time = datetime.now(timezone).strftime('%H:%M:%S')
        bot.reply_to(message, f"В {city.capitalize()} сейчас {current_time}.")
    else:
        bot.reply_to(message, "Извините, я не знаю о таком городе или вы написали его с ошибкой. Попробуйте другой.")

# Запуск бота
bot.polling()