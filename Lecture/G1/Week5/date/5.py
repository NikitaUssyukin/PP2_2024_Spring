import datetime

today = datetime.datetime.now()
yesterday = datetime.datetime.now() - datetime.timedelta(days = 1)

print((today - yesterday).total_seconds())
