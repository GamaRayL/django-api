import requests
from rest_framework import status


def convert_currencies(rub_price):
    usd_price = 0
    response = requests.get(
        url='https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/usd/rub.json'
    )
    if response.status_code == status.HTTP_200_OK:
        usd_rate = response.json()['rub']
        usd_price = rub_price * usd_rate
    return usd_price
