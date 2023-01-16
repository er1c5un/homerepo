import json

import requests as re

'''http://api.exchangeratesapi.io/v1/latest

    ? access_key = YOUR_ACCESS_KEY
    & base = GBP
    & symbols = USD,AUD,CAD,PLN,MXN'''


def main():
    test_url = 'https://min-api.cryptocompare.com/data/blockchain/list'
    my_params = {'access_key': 'd1bcddbbe61fccc7bb193c6e19de6229e220b22ed45e203df468f9e84a4bc065'
                 }
    my_params2 = {'access_key': 'dc778207cbfc3462ec1caee643926cdb'}
    result = re.get(test_url, params=my_params).content
    res = json.loads(result)
    print(res)
    #print('Response', res['Response'])
    #print('Message', res['Message'])
    #print('HasWarning', res['HasWarning'])
    #print('Type', res['Type'])
    #print('RateLimit', res['RateLimit'])
    #for key in res['Data']['exchanges']:
    #    print('KEY = ', key)


if __name__ == '__main__':
    main()
