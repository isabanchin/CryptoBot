import requests
import json
from config import keys, api_key


class APIException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == base:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base}')
        
        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}')
        
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        # print(json.loads(r.content))
        total_base = round(json.loads(r.content)[keys[base]] * amount, 2)
        # print(type(total_base))

        # получение всех валют API
        # k = requests.get(f'https://min-api.cryptocompare.com/data/blockchain/list?api_key={api_key}')
        # get_keys = json.loads(k.content)
        # print(get_keys)
        # print(len(get_keys))

        return total_base