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

    def __init__(self, base_url: str = ''):
        base_url = base_url

    @staticmethod
    def get_price(base: str = None, quote: str = None, amount: int = 1):
        base = base.upper()
        quote = quote.upper()
        try:
            amount = int(amount)
        except ValueError:
            raise ParametersErrorException(f'Упс, похоже количество валюты введено некорректно')

        if base not in codes and base not in additional_codes and base not in crypto_codes:
            raise NonExistingCurrencyException(f'Упс, я не знаю валюты {base}...')
        if quote not in codes and quote not in additional_codes and quote not in crypto_codes:
            raise NonExistingCurrencyException(f'Упс, я не знаю валюты {quote}...')
        res = ExchangeService.http_request(base, quote)
        if res.get('Response') != 'Error':
            print(res)
            print(f'Converting result = {res[quote] * int(amount)}')
            if amount == 1:
                res = f'{additional_codes.get(base, crypto_codes.get(base))} равен {res[quote]} {quote}'
            else:
                res = f'{amount} {base} это {res[quote] * int(amount)} {quote}'
            return res
        else:
            raise APIException(f'Упс, ошибка валютного сервиса...\n{res.get("Message")}')

    @staticmethod
    def auto_convert_to_rub(base):
        base = base.upper()
        quote = 'RUB'
        if base not in codes and base not in additional_codes and base not in crypto_codes:
            raise NonExistingCurrencyException(f'Упс, я не знаю валюты {base}...')
        res = ExchangeService.http_request(base, quote)
        if res.get('Response') != 'Error':
            print(f'Converting result = {res["RUB"]}')
            res = f'{additional_codes.get(base, crypto_codes.get(base))} равен {str(res["RUB"])} RUB'
            return res
        else:
            raise APIException(
                f'Упс, ошибка валютного сервиса...\n{res.get("Message")}')

    @staticmethod
    def http_request(base, quote):
        convert_url = f'https://min-api.cryptocompare.com/data/price?fsym={base}&tsyms={quote}'
        res = json.loads(requests.get(convert_url).content)
        return res


if __name__ == '__main__':
    ex = ExchangeService()
    ex.get_price(base='BTC', quote='RUB')
