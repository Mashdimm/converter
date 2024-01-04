import requests
from bs4 import BeautifulSoup

def take_rate(currency):
    response = requests.get(currency)
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.content, "lxml")

    try:
        rate = soup.find("div", class_="BNeawe iBp4i AP7Wnd").text.split()[0]
    except Exception as e:
        print(e)
    return float(rate.replace(',', '.'))


print()
