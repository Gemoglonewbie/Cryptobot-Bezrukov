import requests
import json
from config import values


class APIException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def convert(base: str, quote: str, amount: str):

        if base == quote:
            raise APIException(f'Введите разные значения валют: {base}-{quote}')

        try:
            base_ticker = values[base]
        except KeyError:
            raise APIException(f'Не удалось обработать введённую валюту {base}')

        try:
            quote_ticker = values[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать введённую валюту {quote}')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать введённую денежную сумму {amount}')

        # response = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={base_ticker}&tsyms={quote_ticker}')

        ###################################### использую свой API ######################################################
        url = (f"https://api.apilayer.com/fixer/convert?to={quote_ticker}&from={base_ticker}&amount={amount}")
        
        payload = {}
        headers= {
        "apikey": "jA8m1njEedXruBLwLfHQTr7jFGi78j9W"
        }
        response = requests.request("GET", url, headers=headers, data = payload)
        
        status_code = response.status_code
        result = response.text
        ################################################################################################################
        # result = json.loads(response.content)[values[quote]]
        # result *= amount

        return result