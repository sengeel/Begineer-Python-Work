import json
from datetime import datetime

class User:
    def __init__(self, username, email, joined):
        self.username = username
        self.email = email
        self.joined = joined

    def __repr__(self):
        return f"User(username={self.username}, email={self.email}, joined={self.joined})"

# Custom object_hook function
def user_hook(dct):
    if 'username' in dct and 'email' in dct and 'joined' in dct:
        joined = datetime.fromisoformat(dct['joined'])
        return User(dct['username'], dct['email'], joined)
    return dct

json_str = '{"username": "john_doe", "email": "john@example.com", "joined": "2021-01-01T00:00:00"}'

# Deserialize JSON string to User object
user = json.loads(json_str, object_hook=user_hook)
print(user)  # Output: User(username=john_doe, email=john@example.com, joined=2021-01-01 00:00:00)


from datetime import datetime

# Define the dates in day-month-year format
date_format = "%d-%m-%Y %H:%M:%S"
date1_str = "27-06-2023 14:30:00"
date2_str = "28-06-2023 16:45:00"

# Convert the strings to datetime objects
date1 = datetime.strptime(date1_str, date_format)
date2 = datetime.strptime(date2_str, date_format)

# Calculate the difference between the dates
date_difference = date2 - date1

# Output the difference in days and seconds
print(f"The difference between the dates is {date_difference.days} days and {date_difference.seconds} seconds.")

# To get the total difference in seconds
total_seconds = date_difference.total_seconds()
print(f"The total difference in seconds is {total_seconds} seconds.")
 




import json
from datetime import datetime

class User:
    def __init__(self, username, email, joined):
        self.username = username
        self.email = email
        self.joined = joined

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Custom serialization function
def serialize(obj):
    if isinstance(obj, User):
        return {
            "username": obj.username,
            "email": obj.email,
            "joined": obj.joined.isoformat()
        }
    elif isinstance(obj, datetime):
        return obj.isoformat()
    
    elif isinstance(obj, Point):
        return{
            "x-axis": obj.x,
            "y-axis": obj.y
        }
    # Raise a TypeError for any other types
    raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")

user = User("john_doe", "john@example.com", datetime(2021, 1, 1))
point = Point(1, 2)

with open ("serial.json", 'w') as file:
    json.dump(user, file, default=serialize, indent=4)
    json.dump(point,file, default=serialize, indent=4)


# Serialize User object to JSON (works)
# json_str_user = 
# print(json_str_user)

# Attempt to serialize Point object to JSON (raises TypeError)

# json_str_point = 
# print(json_str_point)

import pytz
from datetime import datetime

wishes = '%A %d %B %Y %H:%M:%S:%f'
date_obj = 'Friday 28 June 2024 18:47:22:12345'


dressing = datetime.strptime(date_obj, wishes)


naive_datetime = datetime(2024, 6, 28, 17, 29,0,0)

timezone = pytz.timezone('US/Eastern')
sense = datetime.now().today()
brain = sense.strftime('%Y-%m-%d %H:%M:%S:%f')

# Localize the naive datetime to the specified timezone
active_zone = timezone.localize(naive_datetime)
format_active_zone = active_zone.strftime('%d %B %Y %H:%M:%S')

# Format the naive datetime for better display
formatted_naive_datetime = naive_datetime.strftime('%Y-%B-%d %H:%M:%S')
print(f"Trying something out: {brain}")
print(f"Naive datetime: {formatted_naive_datetime}")
print(f"Localized datetime: {format_active_zone}")
print(dressing)

from datetime import datetime
from dateutil import tz

# Create timezone objects
eastern = tz.gettz('US/Eastern')
london = tz.gettz('Europe/London')

# Create aware datetime objects
aware_dt = datetime(2023, 6, 28, 12, 0, tzinfo=eastern)
print("Eastern time:", aware_dt)

# Convert to another timezone
london_dt = aware_dt.astimezone(london)
print("London time:", london_dt)




from datetime import tzinfo, timedelta, datetime

class SimpleTZ(tzinfo):
    def __init__(self, offset, name):
        self.offset = timedelta(hours=offset)
        self.name = name

    def utcoffset(self, dt):
        return self.offset

    def dst(self, dt):
        return timedelta(0)

    def tzname(self, dt):
        return self.name

# Example usage
simple_tz = SimpleTZ(-5, 'EST')
dt = datetime(2023, 6, 28, 12, 0, tzinfo=simple_tz)

print("Custom timezone datetime:", dt)
print("UTC offset:", dt.utcoffset())
print("Timezone name:", dt.tzname())






    












            








