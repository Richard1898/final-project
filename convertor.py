import telebot
from telebot import types
from currency_converter import CurrencyConverter


bot = telebot.TeleBot('7065965994:AAEpECQJ_sIvPCHAzkcak6OhbEPiP1sOZlY')
currency = CurrencyConverter()
amount = 0




@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Добрый день, введите сумму')
    bot.register_next_step_handler(message, summa)

def summa(message):
    global amount
    try:
        amount= int(message.text.strip())
    except ValueError:
        bot.send_message(message.chat.id,'Введите сумму неврный формат')
        bot.register_next_step_handler(message, summa)
        return

    if amount > 0:
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton('EUR/USD',callback_data='eur/usd')
        btn2 = types.InlineKeyboardButton('EUR/GBP',callback_data='eur/gbp')
        btn3 = types.InlineKeyboardButton('EUR/CNY',callback_data='eur/cny')
        btn4 = types.InlineKeyboardButton('Другое значение',callback_data='else')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id,'Выберите валюты из какой в какуй перевести (символику валюты)', reply_markup=markup)
    else:
        bot.send_message(message.chat.id,'Число должно быть больше нуля. Впишите сумму')
        bot.register_next_step_handler(message, summa)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data!='else':
        values = call.data.upper().split('/')
        res = currency.convert(amount, values[0], values[1])
        bot.send_message(call.message.chat.id, f'Получаеться: {round(res, 2)}. Можете заново вписывать сумму')
        bot.register_next_step_handler(call.message, summa)
    else:
        bot.send_message(call.message.chat.id, 'Введите пару валют через слэш напривер(GBP/USD)')
        bot.register_next_step_handler(call.message, mycurrency)


def mycurrency(message):
    try:
        values = message.text.upper().split('/')
        res = currency.convert(amount, values[0], values[1])
        bot.send_message(message.chat.id, f'Получаеться: {round(res, 2)}. Можете заново вписывать сумму')
        bot.register_next_step_handler(message, summa)
    except Exception:
        bot.send_message(message.chat.id, 'не получилось. Можете заново вписывать значения')
        bot.register_next_step_handler(message, mycurrency)
bot.polling(none_stop=True)