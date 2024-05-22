import telebot
from telebot import types
from currency_converter import CurrencyConverter
import json
import os


bot = telebot.TeleBot('7065965994:AAEpECQJ_sIvPCHAzkcak6OhbEPiP1sOZlY')
currency = CurrencyConverter()
amount = 0

# Функция для регистрации данных преобразования в JSON
def log_conversion(amount, from_currency, to_currency, result):
    log_entry = {
        "amount": amount,
        "from_currency": from_currency,
        "to_currency": to_currency,
        "result": result
    }
    if os.path.exists('conversion_log.json'):
        with open('conversion_log.json', 'r+') as file:
            data = json.load(file)
            data.append(log_entry)
            file.seek(0)
            json.dump(data, file, ensure_ascii=False, indent=4)
    else:
        with open('conversion_log.json', 'w') as file:
            json.dump([log_entry], file, ensure_ascii=False, indent=4)

# Запуск обработчика команд
@bot.message_handler(commands=['start'])
def start(message):
    
    bot.send_message(message.chat.id, 'Добрый день, введите сумму')
    bot.register_next_step_handler(message, get_amount)

# Функция для получения суммы от пользователя
def get_amount(message):
    
    global amount
    try:
        amount = int(message.text.strip())
    except ValueError:
        bot.send_message(message.chat.id, 'Введите сумму в правильном формате')
        bot.register_next_step_handler(message, get_amount)
        return
#валидация
    if amount > 0:
        show_currency_options(message)
    else:
        bot.send_message(message.chat.id, 'Число должно быть больше нуля. Впишите сумму')
        bot.register_next_step_handler(message, get_amount)

# Функция отображения вариантов конвертации валют
def show_currency_options(message):
    
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton('EUR/USD', callback_data='eur/usd')
    btn2 = types.InlineKeyboardButton('EUR/GBP', callback_data='eur/gbp')
    btn3 = types.InlineKeyboardButton('EUR/CNY', callback_data='eur/cny')
    btn4 = types.InlineKeyboardButton('Другое значение', callback_data='else')
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id, 'Выберите валюты для конвертации', reply_markup=markup)

# Обработчик обратного вызова для конвертации валюты
@bot.callback_query_handler(func=lambda call: True)
def handle_currency_conversion(call):
    # Обработчик обратного вызова для конвертации валюты
    if call.data != 'else':
        values = call.data.upper().split('/')
        convert_currency(call.message, values[0], values[1])
    else:
        bot.send_message(call.message.chat.id, 'Введите пару валют через слэш, например (GBP/USD)')
        bot.register_next_step_handler(call.message, custom_currency)

# Функция для обработки пользовательской конвертации валютных пар
def custom_currency(message):
    #валидация
    try:
        values = message.text.upper().split('/')
        convert_currency(message, values[0], values[1])
    except Exception:
        bot.send_message(message.chat.id, 'Неправильный формат. Пожалуйста, введите значения заново')
        bot.register_next_step_handler(message, custom_currency)

# Функция для выполнения конвертации валюты
def convert_currency(message, from_currency, to_currency):
    #валидация
    try:
        result = currency.convert(amount, from_currency, to_currency)
        log_conversion(amount, from_currency, to_currency, result) 
        bot.send_message(message.chat.id, f'Получается: {round(result, 2)}. Можете заново вписать сумму')
        bot.register_next_step_handler(message, get_amount)
    except Exception as e:
        bot.send_message(message.chat.id, f'Ошибка конвертации: {str(e)}. Пожалуйста, попробуйте снова')
        bot.register_next_step_handler(message,convert_currency)
bot.polling(none_stop=True)