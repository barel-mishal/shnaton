import io
import requests
from bs4 import BeautifulSoup
from exem import Exem
from google_calnder import GoogleCalender

class Shnaton():
    def get_exems(self, course):
        link = requests.get(f"https://shnaton.huji.ac.il/index.php?peula=CourseD&course={course}&detail=examDates&year=2020&line=&faculty=8&maslul=0")
        html = link.text

        soup = BeautifulSoup(html, features="html.parser")
        rows = soup.select("td.courseTab_content tr")

        exems = set()
        
        for row in rows:
            column = row.select("td.courseTab_td")
            if column:
                exem = Exem()
                exem.name = column[4].get_text()
                exem.date = column[0].get_text()
                exem.time = column[1].get_text()
                exem.simster = column[5].get_text()
                exems.add(exem)
        return exems

