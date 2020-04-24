import requests
from bs4 import BeautifulSoup
import io


# Hi Barel, whats up?
link = requests.get("https://shnaton.huji.ac.il/index.php?peula=Simple&maslul=0&shana=0&year=2020&course=71012")
text = link.text

soup = BeautifulSoup(text, features="html.parser")
print(soup.find(id="mainmenu"))

with io.open("out1.html", "w", encoding="utf-8") as f:
    f.write(text.replace("windows-1255", "utf-8"))
f.close()
