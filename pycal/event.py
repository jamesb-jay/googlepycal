from datetime import datetime as timepoint

TIME_FORMAT = '%Y-%m-%dT%H:%M:%S%z'

class Event:

    def GetEvents(self, timeFrom: timepoint, timeTo: timepoint, service, calendarId):
        service_results = service.events().list(calendarId=calendarId, 
                                            timeMin=self._convert_date(timeFrom), 
                                            timeMax=self._convert_date(timeTo), 
                                            singleEvents=True,
                                            orderBy='startTime').execute()
        
        events = service_results.get("items", [])
        returnList = []

        for e in events:
            returnList.append(
                Event.GetEventFromId(service, calendarId, e.get("id"))
            )
        
        return returnList

    def GetEventFromId(service, calendarId, eventId):
        service_event = service.events().get(calendarId=calendarId, eventId=eventId).execute()
        newEvent = Event(service, calendarId)

        newEvent.parse_timestamps(service_event["start"].get("dateTime"), service_event["end"].get("dateTime"))
        newEvent.summary = service_event.get("summary")
        newEvent.eventId = service_event.get("id")

        return newEvent
    



    service = None
    calendarId = None
    eventId = None

    start = None
    end = None

    summary = None
    colorId = None

    def __init__(self, service, calendarId) -> None:
        self.service = service
        self.calendarId = calendarId

    def parse_timestamps(self, startTime: str, endTime: str):
        self.set_timepoints(
            timepoint.strptime(startTime, TIME_FORMAT),
            timepoint.strptime(endTime, TIME_FORMAT)
        )

    def set_timepoints(self, startTime: timepoint, endTime: timepoint):
        self.start = startTime
        self.end = endTime

    def set_color(self, colorId):
        self.colorId = colorId

    def get_colors_key(service):
        colors =  service.colors().get().execute()
        for id, col in colors['event'].items():
            print(f"colorId: {id}\n  Fg -> {col['foreground']}\n  Bg -> {col['background']}")
        
    @property
    def valid(self):
        return self.service and self.calendarId

    @property
    def body(self):
        return {
                'summary': self.summary,
                'colorId': self.colorId,
                'start': {
                    'dateTime': self.start.strftime(TIME_FORMAT),
                    'timeZone': 'Europe/London',
                },
                'end': {
                    'dateTime': self.end.strftime(TIME_FORMAT),
                    'timeZone': 'Europe/London',
                },
                }

    @property
    def startEndFormatted(self):
        start = self.start.strftime("%d %b %Y")
        end = self.end.strftime("%d %b %Y")

        return f"{start} to {end}"

    def __str__(self) -> str:
        return f"<< ({self.eventId}) {self.summary} : {self.startEndFormatted} >>"
    
    def __repr__(self) -> str:
        return super().__repr__() + f": {self}" 