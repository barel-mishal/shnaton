import requests
from bs4 import BeautifulSoup
import io


# Hi Barel, whats up?
link = requests.get("https://shnaton.huji.ac.il/index.php?peula=CourseD&course=71012&detail=examDates&year=2020&line=&faculty=8&maslul=0")
text = link.text

soup = BeautifulSoup(text, features="html.parser")
rows = soup.select("td.courseTab_content tr")
# Comment
class Exam:
    pass

exams = []

for row in rows:
    columns = row.select("td.courseTab_td")
    if columns:
        exam = Exam()
        exam.name = columns[2].get_text()
        exam.date = columns[0].get_text()
        exam.time = columns[1].get_text()
        exam.simester = columns[5].get_text()
        exams.append(exam)

for exam in exams:
    print("Course name: " + exam.name)
    print("Date: " + exam.date)
    print("Time: " + exam.time)
    print("Simester: " + exam.simester)
    print("-----------------------------\n")

with io.open("out1.html", "w", encoding="utf-8") as f:
    f.write(text.replace("windows-1255", "utf-8"))
f.close()
