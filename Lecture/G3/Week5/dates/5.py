import datetime

today = datetime.datetime.now()

today_without_seconds = today.replace(second=0, microsecond=0)
print(today, today_without_seconds)