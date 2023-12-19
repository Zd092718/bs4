from bs4 import BeautifulSoup
import lxml

with open("website.html", encoding="utf-8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'lxml')
# print(soup.title)
# print(soup.title.string)
# print(soup)
# print(soup.a)