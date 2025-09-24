import requests
import json


def rates_from_json(current: str) -> float:
    try:
        return round(1 / json.loads(requests.get('https://v6.exchangerate-api.com/v6/ddae88ca5e3b35d3695ebc2f/latest/EUR').text)['conversion_rates'][current], 5)

    except:
        return False


