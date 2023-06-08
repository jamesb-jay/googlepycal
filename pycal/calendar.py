from datetime import datetime as timepoint

from .event import Event

class Calendar:
    calendarId = None
    service = None

    def __init__(self, service, calendarId) -> None:
        self.service = service
        self.calendarId = calendarId
    
    def get_events(self, timeFrom: timepoint, timeTo: timepoint):
        service_results = self.service.events().list(calendarId=self.calendarId, 
                                            timeMin=self._convert_date(timeFrom), 
                                            timeMax=self._convert_date(timeTo), 
                                            singleEvents=True,
                                            orderBy='startTime').execute()
        
        events = service_results.get("items", [])

        returnList = []

        for e in events:
            newEvent = Event()
            newEvent.description = e["summary"]
            newEvent.parse_timestamps(e["start"].get("dateTime"), e["end"].get("dateTime"))
            returnList.append(newEvent)
        
        return returnList


    def _convert_date(self, date) -> str:
        assert isinstance(date, timepoint)

        return date.isoformat() + "Z"
    