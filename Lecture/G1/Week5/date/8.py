import datetime

date_str = input()

date = datetime.datetime.strptime(date_str, "%d/%m/%Y, %H:%M:%S")

print(date)


