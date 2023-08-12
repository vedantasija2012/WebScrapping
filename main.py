import requests
from bs4 import BeautifulSoup

# query = input("Enter Name of Place: ")
query = "london"
url = f'https://www.google.com/search?q=weather+{query}'

response = requests.get(
  url,
  headers={
    'User-Agent':
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
  })

soup = BeautifulSoup(response.content, 'html.parser')

# print(soup)

unit = soup.find("span", {'class': "wob_t"})
time = soup.find("span", {'class': 'wob_dts', 'id': "wob_dts"})
weatherDesc = soup.find("span", {'id': "wob_dc"})
temp = soup.find("span", {"class":"wob_t q8U8x", "id":"wob_tm"})

print(query, time, temp, unit, weatherDesc)