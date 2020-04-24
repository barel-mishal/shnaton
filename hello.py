import requests
from bs4 import BeautifulSoup
import io
import re


link = requests.get("https://shnaton.huji.ac.il/index.php?peula=CourseD&course=71012&detail=examDates&year=2020&line=&faculty=8&maslul=0")
text = link.text

soup = BeautifulSoup(text, features="html.parser")
# print(soup.find(id="mainmenu"))
table = soup.select("td.courseTab_content")
list_datatable = []
for i in table:
	list_datatable = i.select("td.courseTab_td")
for i in list_datatable[0::6]:
	print(i) # to try regular exprtion to catch the date


	
with io.open("out1.html", "w", encoding="utf-8") as f:
    f.write(text.replace("windows-1255", "utf-8"))
f.close()


