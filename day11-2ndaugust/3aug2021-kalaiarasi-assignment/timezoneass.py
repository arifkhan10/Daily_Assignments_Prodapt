import pytz
from datetime import datetime
standard_time=pytz.utc
time_zone=pytz.timezone("Asia/Kolkata")
time_zone2=pytz.timezone("America/Mexico_city")
time_zone3=pytz.timezone("Africa/Asmara")
time_zone4=pytz.timezone("Europe/Athens")
time_zone5=pytz.timezone("Japan")
print(datetime.now(time_zone))
print(datetime.now(time_zone2).strftime("%Y-%m-%d %H:%M:%S"))
print(datetime.now(time_zone3).strftime("%Y-%m-%d %H:%M:%S"))
print(datetime.now(time_zone4).strftime("%Y-%m-%d %H:%M:%S"))
print(datetime.now(time_zone5).strftime("%Y-%m-%d %H:%M:%S"))
print(datetime.now(standard_time))
