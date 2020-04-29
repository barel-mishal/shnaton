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

course = "71034"
link = requests.get(f"https://shnaton.huji.ac.il/index.php?peula=CourseD&course={course}&detail=examDates&year=2020&line=&faculty=8&maslul=0")
html = link.text


soup = BeautifulSoup(html, features="html.parser")
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

unique_exems = []
unique_detes = []
for exem in exems:
	if exem.date not in unique_detes:
		unique_detes.append(exem.date)
		unique_exems.append(exem)

for exem in unique_exems:
  parsed_date = exem.date.split("-")
  year = parsed_date[2]
  day = parsed_date[1]
  month = parsed_date[0]
  event = {
    'summary': i.name,
    'description': course_details + "הצלחה מובטחת",
    'start': {
      'date': f'{year}-{month}-{day}',
    },
    'end': {
      'date': f'{year}-{month}-{day}',
    }
  }

  event = service.events().insert(calendarId='primary', body=event).execute()


with io.open("out1.html", "w", encoding="utf-8") as f:
    f.write(text.replace("windows-1255", "utf-8"))
f.close()


