import io
import requests
from bs4 import BeautifulSoup
from exem import Exem
from google_calnder import GoogleCalender

class Shnaton():
    def get_course_hours(self, course):
        link = requests.get(f"https://shnaton.huji.ac.il/index.php?peula=Simple&starting=1&negishut=0&year=2020&course={course}&faculty=0&prisa=2&word=&option=1&coursetype=0&language=&shiur=")
        html = link.text

        soup = BeautifulSoup(html, features="html.parser")
        name_course_eng = soup.select("td.courseTD b")[0].get_text()
        name_course_heb = soup.select("td.courseTD b")[1].get_text()
        
        return name_course_heb

    def get_exems(self, course):
        link = f"https://shnaton.huji.ac.il/index.php?peula=Simple&starting=1&negishut=0&year=2020&course={course}&faculty=0&prisa=2&word=&option=1&coursetype=0&language=&shiur="
        main_page = requests.get(link)
        main_html = main_page.text
        soup = BeautifulSoup(main_html, features="html.parser")
        name_course_eng = soup.select("td.courseTD b")[0].get_text()
        name_course_heb = soup.select("td.courseTD b")[1].get_text()
        
        exem_page = requests.get(f"https://shnaton.huji.ac.il/index.php?peula=CourseD&course={course}&detail=examDates&year=2020&line=&faculty=8&maslul=0")
        exem_html = exem_page.text

        soup = BeautifulSoup(exem_html, features="html.parser")
        rows = soup.select("td.courseTab_content tr")

        exems = set()
        
        for row in rows:
            column = row.select("td.courseTab_td")
            if column:
                exem = Exem()
                exem.course_link = link
                exem.course_name_eng = name_course_eng
                exem.name_course_heb = name_course_heb
                exem.name = column[4].get_text()
                exem.date = column[0].get_text()
                exem.time = column[1].get_text()
                exem.simster = column[5].get_text()
                exems.add(exem)
        return exems
    
    def get_class_time():
        pass

    

