##############################################################################
# Arithmetic Operators with Dates and Strings, by operators.
##############################################################################

import datetime

one_day = datetime.timedelta(days=1)
today_date = datetime.date.today()
print("Data ingestion date is:", today_date)
tomorrow_date = today_date + one_day
print("SEO target output keyword date is:", tomorrow_date)

print("\n")

first_name = "Keith "
last_name = "Otto"
full_name = first_name + last_name
print(full_name, "used to be at ADOBE.")

print("\n")

last_names = ("Otto", "McGill")
first_names = ("Keith", "Dominique")
print(first_names * 2)
print(last_names + first_names * 5)
















