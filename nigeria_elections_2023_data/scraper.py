from bs4 import BeautifulSoup
import requests


URL = "https://en.wikipedia.org/wiki/2023_Nigerian_presidential_election#By_state"
page_source = requests.get(URL)


soup = BeautifulSoup(page_source.content, "lxml")

print(title := soup.title)
TABLE_HEADERS = soup.select("table:nth-of-type(14) >  thead")
print(TABLE_HEADERS)

# c = soup.find_all(class_="wikitable sortable jquery-tablesorter")
# print(c)

