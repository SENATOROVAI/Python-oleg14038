import sys; sys.path.append("/path/to/root")
from requests import re
import os
import json



API_KEY = "bce823840b2ba077be0b77fe90e64a22"
url = "https://api.exchangeratesapi.io/v1/"


BASE_CURRENCY = "EUR"  # only for free tariff
OUTPUT_CURRENCY_LIST = "USD", "EUR"
AMOUNT = 1

def exchange(cur, amount):
    with open('exchangerates_req.json') as f:
        req_json = json.loads(f.readlines())
        result = float(req_json['rates']['cur'])
    return f"{amount} EUR = {result} {cur}"

def currency(currency):
    """
    This function returns a nested function that takes an 'amount' as input, 
    extracts the exchange rate for a given 'currency' from a JSON file,
    and returns the converted amount.
    """
    def among(amount):
        nonlocal currency
        cur = currency
        with open('exchangerates_req.json') as f:
            req_json = json.loads(f.readlines())
        return float(req_json['rates']['cur'])
    return among


get_cuttency = currency("RUB")
print(currency("USD")(2))
print(get_cuttency(5))
