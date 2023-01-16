import telebot
from config import TOKEN, codes, additional_codes, crypto_codes
from extensions import ExchangeService, NonExistingCurrencyException, ParametersErrorException, APIException

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def hello_func(message):
    text = 'чтобы начать, напишите:\n' \
           '<имя валюты> - вы получите ее текущий курс в рублях\n' \
           '<имя валюты> <в какую валюту перевести> - чтобы узнать курс пары\n' \
           '<имя валюты> <в какую валюту перевести> <количество> - чтобы сразу перевести определенную сумму\n\n' \
           'Курсы криптовалют тоже доступны.\n\n' \
           'Команды:\n' \
           '/values - список основных валют\n' \
           '/all_values - все валюты\n' \
           '/crypto - список криптовалют'
    bot.reply_to(message, f"{message.from_user.first_name}, {text}")


@bot.message_handler(commands=['values'])
def handle_values_cmd(message):
    text = 'Основные валюты:'
    for key in codes.keys():
        text += '\n' + key + ' - ' + codes[key]
    bot.reply_to(message, text)


@bot.message_handler(commands=['crypto'])
def handle_values_cmd(message):
    text = 'Криптовалюты:'
    for key in crypto_codes.keys():
        text += '\n' + key + ' - ' + crypto_codes[key]
    bot.reply_to(message, text)


@bot.message_handler(commands=['all_values'])
def handle_values_cmd(message):
    text = 'Полный список валют:'
    for key in additional_codes.keys():
        text += '\n' + key + ' - ' + additional_codes[key]
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def convert(message):
    try:
        message_list = message.text.split()
        if len(message_list) == 1:
            base = message_list[0]
            result = api.auto_convert_to_rub(base)
            print('result = ', result)
        elif len(message_list) == 2:
            base = message_list[0]
            quote = message_list[1]
            result = api.get_price(base, quote)
        elif len(message_list) == 3:
            base = message_list[0]
            quote = message_list[1]
            amount = message_list[2]
            result = api.get_price(base, quote, amount)
        else:
            raise ParametersErrorException(f'Упс, похоже, вы ввели слишком много параметров...')
    except NonExistingCurrencyException as e:
        result = e
    except ParametersErrorException as e:
        result = e
    except APIException as e:
        result = e
    except Exception as e:
        result = f'Не удалось обработать команду.\nОшибка:{str(e)}'
    bot.reply_to(message, result)


api = ExchangeService()
bot.polling(non_stop=True)
