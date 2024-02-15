import datetime

today = datetime.datetime.now()
yesterday = today - datetime.timedelta(days=1)

print(yesterday)

# diff between 2 days
diff = today - yesterday
print(diff)