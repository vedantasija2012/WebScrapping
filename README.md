# Web Scrapping

Web scrapping is way of getting data from the web. All you do is just make a get() request and then python takes care of everything else.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requests module and BeautifulSoup library.

```bash
pip install requests
pip install BeautifulSoup
```

## Usage

```python
import requests
from bs4 import BeautifulSoup
```

This get() request returns data in html format
```python
response = requests.get(
  url,
  headers={
    'User-Agent':
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
  })
```
Using BeautifulSoup to parse html.
```python
soup = BeautifulSoup(response.content, 'html.parser')
```

Finding span and div with respective id and class.
```python
temp = soup.find("span", {'class': "wob_t q8U8x", 'id': "wob_tm"})
unit = soup.find("span", {'class': "wob_t"})
time = soup.find("span", {'class': 'wob_dts', 'id': "wob_dts"})
weatherDesc = soup.find("span", {'id': "wob_dc"})
```

Printing the data we have recived.
```python
print(query, time, temp, unit, weatherDesc)
```
