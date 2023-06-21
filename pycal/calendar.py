from datetime import datetime as timepoint

from .event import Event

class Calendar:
    calendarId = None
    service = None

    def __init__(self, service, calendarId) -> None:
        self.service = service
        self.calendarId = calendarId
    
    def get_events(self, timeFrom: timepoint, timeTo: timepoint) -> list[Event]:
        return Event.GetEvents(timeFrom, timeTo, self.service, self.calendarId)

    def get_event_by_id(self, eventId) -> Event:
        return Event.GetEventFromId(self.service, self.calendarId, eventId)
    
    def new_event(self) -> Event:
        return Event(self.service, self.calendarId)
