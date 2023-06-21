# googlepycal
A very bad wrapper for the Google Calender API

## Setup
 - Ensure the correct packages are installed (or just run install.bat)
 - Get your `credentials.json` from google APIs
 - `token.json` is created automatically

## Example usage

```Python
from pycal.connection import APIConnection

from datetime import datetime as timepoint
from datetime import timedelta

# Some times for examples
now = timepoint.utcnow()
in1hour = now + timedelta(hours=1)
in2hour = now + timedelta(hours=2)
in1day = now + timedelta(days=1)
in1week = now + timedelta(days=2)


# Create a connection
connection = APIConnection("credentials.json", "token.json")


# Get a calendar using an id
exampleCalendar = connection.get_calendar("primary")


# Get a list of events in given timeframe
eventList = exampleCalendar.get_events(now, in1week)
print(eventList)


# Create event & add to calendar
newEvent = exampleCalendar.new_event()

newEvent.set_timepoints(in1hour, in2hour)
newEvent.summary = "Example 1 hour event"
newEvent.set_color(5)

newEvent.create()


# Update an existing event
newEvent.summary = "Better title for 1 hour event."
newEvent.update()

# Delete the event
newEvent.delete()
```