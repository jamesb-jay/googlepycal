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

            newEvent = Event(e["start"].get("dateTime"), e["end"].get("dateTime"), e.get("summary"))
            newEvent.eventId = e.get("id")
            returnList.append(newEvent)
        
        return returnList

    def get_event_by_id(self, eventId):
        e = self.service.events().get(calendarId=self.calendarId, eventId=eventId).execute()
        newEvent = Event(e["start"].get("dateTime"), e["end"].get("dateTime"), e.get("summary"))
        newEvent.eventId = e.get("id")
        return newEvent
    
    def add_event(self, event: Event):
        createdEvent = self.service.events().insert(calendarId=self.calendarId, body=event.body).execute()
        event.eventId = createdEvent.get("id")
        return event
    
    def update_event(self, event: Event):
        self.service.events().update(calendarId=self.calendarId, eventId=event.eventId, body=event.body).execute()
    
    def delete_event(self, event: Event):
        self.service.events().delete(calendarId=self.calendarId, eventId=event.eventId).execute()

    def _convert_date(self, date) -> str:
        assert isinstance(date, timepoint)

        return date.isoformat() + "Z"
    