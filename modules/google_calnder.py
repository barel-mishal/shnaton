import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

class GoogleCalender():
    def __init__(self):
        # If modifying these scopes, delete the file token.pickle.
        SCOPES = ['https://www.googleapis.com/auth/calendar']

        creds = None

        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)
        self.service = build('calendar', 'v3', credentials=creds)

    def create_exem(self, exem, course_num):
        parsed_date = exem.date.split("-")
        year = parsed_date[2]
        day = parsed_date[0]
        month = parsed_date[1]
        event = {
            'summary': f"{exem.name_course_heb} {exem.name}",
            'description': f"{course_num}\n{exem.course_link}",
            'start': {
                'date': f'{year}-{month}-{day}',
            },
            'end': {
                'date': f'{year}-{month}-{day}',
            }
        }
        event = self.service.events().insert(calendarId='primary', body=event).execute()
        pass

    def create_class():
        pass

