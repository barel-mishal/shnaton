import requests
from bs4 import BeautifulSoup
import io
import re
import quickstart # try to link the two file to work togther i will keep trying

link = requests.get("https://shnaton.huji.ac.il/index.php?peula=CourseD&course=71012&detail=examDates&year=2020&line=&faculty=8&maslul=0")
text = link.text

soup = BeautifulSoup(text, features="html.parser")
rows = soup.select("td.courseTab_content tr")

class Exem():
	pass
		
exems = []
for row in rows:
	column = row.select("td.courseTab_td")
	if column:
	 	exem = Exem()
	 	exem.name = column[4].get_text()
	 	exem.date = column[0].get_text()
	 	exem.time = column[1].get_text()
	 	exem.simster = column[5].get_text()
	 	exems.append(exem)

# i try to make it print one time 

# for exem in exems:
# 		print("name due: " + exem.name)
# 		print("date of exem: " + exem.date)
# 		print("time: " + exem.time)
# 		print("simster: " + exem.date)
# 		print("__________________________\n")

objects = []
date1 = []
for i in exems:
	if i.date not in date1:
		date1.append(i.date)
		objects.append(i)



with io.open("out1.html", "w", encoding="utf-8") as f:
    f.write(text.replace("windows-1255", "utf-8"))
f.close()


