###############################################################################
# for loop examples
###############################################################################

for x in "hello Dominique":
    print(x)
print("\n")
print("The last character is :", x, "Thus the loop terminates")
print("\n")

# For loop with a list iterator
for names in ["John", "Kimmy", "Sam", "Otto", "Dominique"]:
    print (names)
print("The last name is :", names, "Thus the loop terminates.")
print("\n")

# For loop with a Dictionary iterator
for employee_record in {"Name": "John", "Department": "Python", "Salary": 150000}:
    print(employee_record)
    print("The last record key is:", employee_record, "Thus the loop terminates.")

###############################################################################
# While loop
###############################################################################

counter = 0
while counter < 4:
    counter = counter + 1
    print("The Media Group counter is :", counter)
print("The Media Group is now :", counter, "Thus the loop terminates.")
print("\n")




