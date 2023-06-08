from datetime import datetime as timepoint

TIME_FORMAT = '%Y-%m-%dT%H:%M:%S%z'

class Event:

    start = None
    end = None

    summary = None
    eventId = None
    colorId = None
    
    def __init__(self, start, end, summary) -> None:
        if isinstance(start, str):
            self.parse_timestamps(start, end)
        else:
            self.set_timepoints(start, end)
        self.summary = summary

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