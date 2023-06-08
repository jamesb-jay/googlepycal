from datetime import datetime as timepoint

TIME_FORMAT = '%Y-%m-%dT%H:%M:%S%z'

class Event:

    start = None
    end = None

    description = None
    colorId = None
    
    def __init__(self) -> None: ...

    def parse_timestamps(self, startTime: str, endTime: str):
        self.set_timepoints(
            timepoint.strptime(startTime, TIME_FORMAT),
            timepoint.strptime(endTime, TIME_FORMAT)
        )

    def set_timepoints(self, startTime: timepoint, endTime: timepoint):
        self.start = startTime
        self.end = endTime

    @property
    def startEndFormatted(self):
        start = self.start.strftime("%d %b %Y")
        end = self.end.strftime("%d %b %Y")

        return f"{start} to {end}"

    def __str__(self) -> str:
        return f"{self.description}: {self.startEndFormatted}"
    
    def __repr__(self) -> str:
        return super().__repr__() + f": {self}" 