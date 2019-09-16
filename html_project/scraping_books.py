import requests
from bs4 import BeautifulSoup

# page = requests.get('http://books.toscrape.com/')
page = requests.get('http://www.example.com')
# print(page.content)

soup = BeautifulSoup(page.content, 'html.parser')
# print(soup)


print(soup.findAll('h1'))
print(soup.findAll('p'))

locator = 'p a'
print(soup.select_one(locator).attrs['href'])

