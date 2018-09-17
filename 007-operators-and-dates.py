# ############################################################################
# Operators and operator effects on dates; date differences.
# ############################################################################

import datetime

x = 10
y = 2
z = x + y
print(z)
z = x - y
print(z)
z = x / y
print(z)

print("\n")
one_day = datetime.timedelta(days=1)
today_date = datetime.date.today()
print("Thomas Hobbs says - Today’s date is:",today_date)
tomorrow_date = today_date + one_day
print("Thomas Hobbs says - Tomorrow's date is:",tomorrow_date)
yesterday_date = today_date - one_day
print("Thomas Hobbs says - 'Yesterday's date was:", yesterday_date, "'")



