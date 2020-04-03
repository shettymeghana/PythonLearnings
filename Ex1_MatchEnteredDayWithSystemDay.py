#Take input from user as day[like Monday] and check with system day. Display/Print "Yes" if system day match with user entered day.
# Give appropriate error message if user enter any number as input.
import datetime
from datetime import datetime as date
#days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
system_day = date.today().strftime("%A")
user_day = raw_input("Enter day-> ")

if system_day.lower() == user_day.lower():
    print "Yes"
else:
    print "You entered invalid day"
