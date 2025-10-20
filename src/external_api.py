import os
from http.client import responses

import requests
from dotenv import load_dotenv

load_dotenv()


def convert_curr(from_: str, to_: str, trans_amount: str) -> float:
    """Функция обращается к внешнему API и производит конвертацию валюты."""

    API_KEY = os.getenv("API_KEY")


    response = requests.get(
        f"https://api.apilayer.com/exchangerates_data/convert?to={to_}&from={from_}&amount={trans_amount}&apikey={API_KEY}"
    )

    if response.status_code == 200:
        currency_rate = response.json()["info"]["rate"]
        result = response.json()["result"]

    else:
        print("\nЧто-то пошло не так с запросом на конвертацию валюты.")
        result = -1

    return result
