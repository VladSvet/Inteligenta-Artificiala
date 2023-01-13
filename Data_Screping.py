import pandas as pd
import requests
from bs4 import BeautifulSoup

Numele_masinii = []
Prices = []
Description = []

for i in range(2,10):
    url = "https://999.md/ro/list/transport/cars?view_type=detail&page="+str(i)

    r= requests.get(url)
    #print(r)

    soup = BeautifulSoup(r.text, "lxml")
    #box = soup.find("div", class_="items__list__container categories-map detail")

    names = soup.find_all("div", class_="ads-list-detail-item-title")
    for i in names:
     name = i.text
     Numele_masinii.append(name)
print(Numele_masinii)

prices = soup.find_all("div", class_="ads-list-detail-item-price")

for i in prices:
    name = i.text
    Prices.append(name)
print(Prices)

desc = soup.find_all("div", class_="ads-list-detail-item-intro")

for i in desc:
    name= i.text
    Description.append(name)

print(Description)

