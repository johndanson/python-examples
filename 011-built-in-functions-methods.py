##############################################################################
# Built-in functions (methods)
##############################################################################
import math

# function_name(parameters) and with no parameters variable_name.function_name()
# For strings, these are methods like title() for title case, len() for string length, upper() [case] and replace().

name = "Dominique McGill"
print(name.title())
print(len(name))
print(name.upper())

# Data type conversion functions

employee_record = "The employee is called Mia: Cost to employ is:" + str(200000)
print(employee_record)

# Number built-in functions, integer conversion from float

x = 10
y = 3
z = x/y
print("Raw", z)
print("Integer", int(z))

# rounding, high low values

x = 10
y = z = x/y
print("Raw score", z)
print("Min. pass for class", round(z,3))
cx = math.ceil(y)
# get gpa as float
dx = float(cx)
print("Ave. for yr. gp.", math.floor(z))

t = name.replace("Dominique", "GPA")
print(t, "=", dx)






