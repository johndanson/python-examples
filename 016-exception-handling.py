###############################################################################
# Exception Handling
###############################################################################


# no exception
try:
    net_salary3 = 0
    gross_sal = 50000
    tax = gross_sal * 0.20
except ZeroDivisionError:
    print("Dominique - A divide by zero error has occurred. Please try again. ")

else:
    net_salary3 = gross_sal - tax
print(net_salary3)


# handles exception
try:
    net_salary4 = 0
    gross_sal = 50000/0
    tax = gross_sal * 0.20
except ZeroDivisionError:
    print("Dominique - A divide by zero error has occurred. Please try again. ")

else:
    net_salary4 = gross_sal - tax
print(net_salary4)




