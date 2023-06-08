# googlepycal
A very bad wrapper for the Google Calender API

## Setup
 - Ensure the correct packages are installed (or just run install.bat)
 - Get your `credentials.json` from google APIs
 - `token.json` is created automatically

## Example usage

```Python
from pycal.connection import APIConnection
from pycal.event import Event

from datetime import datetime as timepoint
from datetime import timedelta


connection = APIConnection("credentials.json", "token.json")

cal = connection.get_calendar("ph5hgiju22q1pg77fegbc6d5ug")


now = timepoint.utcnow()
in1week = now + timedelta(days=2)
in1day = now + timedelta(days=1)

# Get a list of events
print(cal.get_events(now, in1week))

# Create event
e1 = Event(in1day, in1week, "Intereting summary")
e1.colorId = 5
# Get returned event to update the eventId
e1 = cal.add_event(e1)

# Change an existing event
e1.summary = "Even interestinger summary"
cal.update_event(e1)

# Delete an event
cal.delete_event(e1)
```