import requests
from bs4 import BeautifulSoup

link = requests.get("https://shnaton.huji.ac.il/index.php?peula=Simple&maslul=0&shana=0&year=2020&course=71012")
print(link)
print(link.text)