import requests
from bs4 import BeautifulSoup

# print(BeautifulSoup)


# Hi Barel, whats up?
link = requests.get("https://shnaton.huji.ac.il/index.php?peula=Simple&maslul=0&shana=0&year=2020&course=71012")

soup = BeautifulSoup(link.text, features="html.parser")
print(soup.find(id="mainmenu"))

# print(link)
# print(link.text)