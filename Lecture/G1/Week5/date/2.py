import datetime

yesterday = datetime.datetime.now() - datetime.timedelta(days = 1)

print(yesterday)