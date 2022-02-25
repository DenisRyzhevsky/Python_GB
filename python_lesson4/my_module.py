from requests import get, utils

def currency_rates(valute):
    res = utils.get_unicode_from_response(get("http://www.cbr.ru/scripts/XML_daily.asp"))
    # print(res)
    ht = res.split('Valute ID=')
    # print(ht)
    for el in ht:
        if valute.upper() in el:
            print(valute.upper())
            print(float(el.replace("/", "").split("<Value>")[1].replace(",", ".")))

if __name__ == "__main__":
    currency_rates("usd")

