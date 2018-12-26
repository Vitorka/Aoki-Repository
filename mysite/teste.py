from datetime import datetime

parsed_date = datetime.strptime("2018-11-01", '%Y-%m-%d')
init_d = datetime(parsed_date.year, parsed_date.month, 1)
init_week = init_d.weekday()

day = datetime.strptime("2018-11-04", '%Y-%m-%d')

acc = (init_week + 1) % 7

print(day - init_d)