# ############################################################################
# Python Dates and Time Manipulation
# ############################################################################
import datetime
today_date = datetime.date.today()
today_date_time = datetime.datetime.now()
time_now = datetime.datetime.now().time()


print("Today’s date and time is:", today_date_time)
td = '{:%m-%d-%Y %H:%M:%S}'.format(today_date_time)
print("Today’s date is:", today_date)
td = '{:%H:%M:%S}'.format(today_date_time)
print("Myers Media time is:", td)

# A list of formats

# %a Weekday as locale’s abbreviated name.
# %A Weekday as locale’s full name.
# %w Weekday as a decimal number, where 0 is Sunday and 6 is Saturday.
# %d Day of the month as a zero-padded decimal number.
# %b Month as locale’s abbreviated name.
# %B Month as locale’s full name.
# %m Month as a zero-padded decimal number. 01, ..., 12
# %y Year without century as a zero-padded decimal number. 00, ..., 99
# %Y Year with century as a decimal number. 1970, 1988, 2001, 2013
# %H Hour (24-hour clock) as a zero-padded decimal number. 00, ..., 23
# %I Hour (12-hour clock) as a zero-padded decimal number. 01, ..., 12
# %p Locale’s equivalent of either AM or PM.
# %M Minute as a zero-padded decimal number. 00, ..., 59
# %S Second as a zero-padded decimal number. 00, ..., 59
# %f Microsecond as a decimal number, zero-padded on the left. 000000, ..., 999999
# %z UTC offset in the form +HHMM or -HHMM (empty if naive), +0000, -0400, +1030
# %Z Time zone name (empty if naive), UTC, EST, CST
# %j Day of the year as a zero-padded decimal number. 001, ..., 366
# %U Week number of the year (Sunday is the first) as a zero padded decimal number.
# %W Week number of the year (Monday is first) as a decimal number.
# %c Locale’s appropriate date and time representation.
# %x Locale’s appropriate date representation.
# %X Locale’s appropriate time representation.
# %% A literal '%' character.



