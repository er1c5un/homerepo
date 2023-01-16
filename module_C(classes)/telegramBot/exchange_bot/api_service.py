import requests
import json
from config import codes, additional_codes, crypto_codes


class NonExistingCurrencyException(ValueError):
    pass


class ParametersErrorException(ValueError):
    pass


class APIException(ValueError):
    pass


class ExchangeService:

    def __init__(self, base_url=''):
        base_url = base_url

    @staticmethod
    def get_price(base=None, quote=None, amount=1):
        base = base.upper()
        quote = quote.upper()
        if base not in codes and base not in additional_codes and base not in crypto_codes:
            raise NonExistingCurrencyException(f'Упс, я не знаю валюты {base}...')
        if quote not in codes and quote not in additional_codes and quote not in crypto_codes:
            raise NonExistingCurrencyException(f'Упс, я не знаю валюты {base}...')
        convert_url = f'https://min-api.cryptocompare.com/data/price?fsym={base.upper()}&tsyms={quote.upper()}'
        print(f'Converting {amount} {base} into {quote}')
        res = json.loads(requests.get(convert_url).content)
        if res.get('Response') != 'Error':
            print(res)
            print(f'Converting result = {res[quote] * int(amount)}')
            if amount == 1:
                res = f'{additional_codes.get(base, crypto_codes.get(base))} равен {res[quote] * int(amount)} {quote}'
            else:
                res = f'{amount} {base} это {res[quote] * int(amount)} {quote}'
            return res
        else:
            raise APIException(f'Упс, ошибка валютного сервиса...\n{res.get("Message")}')

    @staticmethod
    def auto_convert_to_rub(base):
        base = base.upper()
        if base not in codes and base not in additional_codes and base not in crypto_codes:
            raise NonExistingCurrencyException(f'Упс, я не знаю валюты {base}...')
        convert_url = f'https://min-api.cryptocompare.com/data/price?fsym={base.upper()}&tsyms=RUB'
        print(f'Converting 1 {base} into RUB')
        res = json.loads(requests.get(convert_url).content)
        if res.get('Response') != 'Error':
            print(f'Converting result = {res["RUB"]}')
            res = f'{additional_codes.get(base, crypto_codes.get(base))} равен {str(res["RUB"])} RUB'
            return res
        else:
            raise APIException(
                f'Упс, ошибка валютного сервиса. Валюта не найдена...\n{res.get("Message")}\nУказанная валюта не найдена')


if __name__ == '__main__':
    ex = ExchangeService()
    ex.get_price(base='BTC', quote='RUB')
