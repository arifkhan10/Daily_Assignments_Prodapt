import pytz
from datetime import datetime

std_time = pytz.utc
time_zone = pytz.timezone("Africa/Bamako")
print(datetime.now(std_time))
print(datetime.now(time_zone))
print((datetime.now(time_zone).strftime("%y:%m:%d%H:%M:%M:%S")))    #for formating the date and time

time_zone2 = pytz.timezone("US/Arizona")
print((datetime.now(time_zone2).strftime("%y:%m:%d%H:%M:%M:%S")))