import requests as re
import json
import os


API_KEY = "3b657357d9c210c7bcee8ce37875e685"
PAIR_CURRENCY = "USDRUB"
AMOUNT = "5"

# 1000 requests in a day
req_ = req.get(f'https://currate.ru/api/?get=currency_list&key={API_KEY}')
get =  "https://currate.ru/api/?get=rates&pairs=USDRUB,EURRUB&key=YOUR-API-KEY"


def get_pair_amount():
    global AMOUNT, PAIR_CURRENCY
    PAIR_CURRENCY, AMOUNT = input(
        "Input currency pair: "), input("Input amount: ")


def get_pair_course():
    req = dict(json.loads(re.get(
        f'https://currate.ru/api/?get=rates&pairs={PAIR_CURRENCY}&key={API_KEY}').text)["data"])
    return req[PAIR_CURRENCY]
# currency list


"""


        "BCHEUR",
        "BCHGBP",
        "BCHJPY",
        "BCHRUB",
        "BCHUSD",
        "BCHXRP",
        "BTCBCH",
        "BTCEUR",
        "BTCGBP",
        "BTCJPY",
        "BTCRUB",
        "BTCUSD",
        "BTCXRP",
        "BTGUSD",
        "BYNRUB",
        "CADRUB",
        "CHFRUB",
        "CNYEUR",
        "CNYRUB",
        "CNYUSD",
        "ETHEUR",
        "ETHGBP",
        "ETHJPY",
        "ETHRUB",
        "ETHUSD",
        "EURAED",
        "EURAMD",
        "EURBGN",
        "EURBYN",
        "EURGBP",
        "EURJPY",
        "EURKZT",
        "EURRUB",
        "EURTRY",
        "EURUSD",
        "GBPAUD",
        "GBPBYN",
        "GBPJPY",
        "GBPRUB",
        "GELRUB",
        "GELUSD",
        "IDRUSD",
        "JPYAMD",
        "JPYAZN",
        "JPYRUB",
        "LKREUR",
        "LKRRUB",
        "LKRUSD",
        "MDLEUR",
        "MDLRUB",
        "MDLUSD",
        "MMKEUR",
        "MMKRUB",
        "MMKUSD",
        "RSDEUR",
        "RSDRUB",
        "RSDUSD",
        "RUBAED",
        "RUBAMD",
        "RUBAUD",
        "RUBBGN",
        "RUBKZT",
        "RUBMYR",
        "RUBNZD",
        "RUBSGD",
        "RUBTRY",
        "RUBUAH",
        "THBCNY",
        "THBEUR",
        "THBRUB",
        "USDAED",
        "USDAMD",
        "USDAUD",
        "USDBGN",
        "USDBYN",
        "USDCAD",
        "USDGBP",
        "USDILS",
        "USDJPY",
        "USDKGS",
        "USDKZT",
        "USDMYR",
        "USDRUB",
        "USDTHB",
        "USDUAH",
        "USDVND",
        "XRPEUR",
        "XRPGBP",
        "XRPJPY",
        "XRPRUB",
        "XRPUSD",
        "ZECUSD"
"""

def refresh_data():
    req_ = re.get(f'https://currate.ru/api/?get=currency_list&key={API_KEY}')
    with open('req_cur.json', 'w') as outfile:
        json.dump(json.loads(get_course.text), outfile, ensure_ascii=False, indent=4)


with open("req.json", "r") as file:
    req_json = json.loads(file.read())
    staus_code = req_json["status"]


if os.path.exists('req_cur.json')==0:
    with open('req_cur.json', 'w') as outfile:
        json.dump(json.loads(get.text), outfile, ensure_ascii=False, indent=4)

with open("req_cur.json", "r") as file:
    req_json = json.loads(file.read())
print(req_json["data"])
