import datetime, calendar
from datetime import timedelta

years = []
for year in range(1006,1996,10):
    if datetime.date(year, 1, 26).weekday() == 0 and calendar.isleap(year):
        years.append(year)

print(years)
data = datetime.date(years[-2], 1, 26)
print(data+timedelta(days=1))
