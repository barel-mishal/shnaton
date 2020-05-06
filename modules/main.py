from shnaton import Shnaton
from google_calnder import GoogleCalender


course = "71056"
google_calnder = GoogleCalender()
shnaton = Shnaton()
exems = shnaton.get_exems(course)

for exem in exems:
    google_calnder.create_exem(exem, course)