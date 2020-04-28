import requests
from bs4 import BeautifulSoup
import io
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']

creds = None
# The file token.pickle stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.
if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)
# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)

service = build('calendar', 'v3', credentials=creds)

course_details = "71430"
link = requests.get(f"https://shnaton.huji.ac.il/index.php?peula=CourseD&course={course_details}&detail=examDates&year=2020&line=&faculty=8&maslul=0")
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

for i in objects:
  x = i.date.split("-")
  event = {
    'summary': i.name,
    'description': course_details,
    'start': {
      'date': f'{x[2]}-{x[1]}-{x[0]}',
      #'timeZone': 'America/Los_Angeles',
    },
    'end': {
      'date': f'{x[2]}-{x[1]}-{x[0]}',
      #'timeZone': 'America/Los_Angeles',
    }
  }

  event = service.events().insert(calendarId='primary', body=event).execute()


with io.open("out1.html", "w", encoding="utf-8") as f:
    f.write(text.replace("windows-1255", "utf-8"))
f.close()


