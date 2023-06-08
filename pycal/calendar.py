import datetime

class Calendar:
    calendarId = None
    service = None

    def __init__(self, service, calendarId) -> None:
        self.service = service
        self.calendarId = calendarId
    

    def _convert_date(self, date) -> str:
        assert isinstance(date, datetime.datetime)

        return date.isoformat() + "Z"
    