from os import path as FilePath

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials as GoogleCreds
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build as build_service

from . import calendar

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
CALENDAR_VERSION = "v3"

class APIConnection:
    credentialsPath = None
    tokenPath = None

    credentials = None
    service = None

    def __init__(self, credentialsPath, tokenPath) -> None:
        self.credentialsPath = credentialsPath
        self.tokenPath = tokenPath

        # Check if token has already been generated:
        if FilePath.exists(tokenPath):
            self.credentials = GoogleCreds.from_authorized_user_file(tokenPath, SCOPES)
        
        # Refresh credentials if needed
        if not self.credentials or not self.credentials.valid:
            self._refresh_credentials()

        self._build_service()
        
    def get_calendar(self, calendarId):
        return calendar.Calendar(self.service, calendarId)

    def _refresh_credentials(self):
        ''' Refresh credentials & generate token '''
        assert self.credentialsPath != None
        assert self.tokenPath != None

        if self.credentials and self.credentials.expired and self.credentials.refresh_token:
            self.credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(self.credentialsPath, SCOPES)
            self.credentials = flow.run_local_server(port=0)
        
        with open(self.tokenPath, 'w') as token:
            token.write(self.credentials.to_json())

    def _build_service(self):
        self.service = build_service("calendar", CALENDAR_VERSION, credentials=self.credentials)
