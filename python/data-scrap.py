import requests
from bs4 import BeautifulSoup

url = 'https://vinitalyplus.com/en/companies/3339_260228864/azienda-agricola-salvetta'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

data = soup.find_all("div", {"class": "enant-VIR"})

for i in data:
    print(i)