import requests
from bs4 import BeautifulSoup
import io



# Hi Barel, whats up?
link = requests.get("https://shnaton.huji.ac.il/index.php?peula=Simple&maslul=0&shana=0&year=2020&course=71012")
with io.open("out1.html", "w", encoding="utf-8") as f:
    f.write(link.text)
f.close()