###############################################################################
# User defined functions
###############################################################################


# Begins with the def keyword then function name, braces and tends with a colon.
# The results are delivered via the return keyword.
# The following example shows 2 user defined functions


def getdate():
    import datetime
    today_date = datetime.date.today()
    return today_date

    today_date = getdate
    print("Today's date at MMG is :", today_date)


def net_salary(gross_sal):
    tax = gross_sal * 0.20
    net_salary2 = gross_sal - tax
    return net_salary2
    net_salary2 = Netsalary2(40000)
    print("The MMG net salary is :", net_salary2)



