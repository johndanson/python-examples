# ############################################################################
# Text string function with mid left right, strip, left strip right strip.
# ############################################################################


def printnames(xnameitems, leftwidth, rightwidth):
    print('Brand name items'.center(leftwidth + rightwidth, '-'))
    for k, v in xnameitems.items():
        print(k.ljust(leftwidth, '.') + str(v).rjust(rightwidth))


nameitems = {'myers': 4, 'media': 12, 'group': 4, 'internet': 80}
printnames(nameitems, 12, 5)
printnames(nameitems, 20, 6)

print("\n")
employee_name = 'Dominique McGill'
print("First Name: ", "\t", employee_name[0:9]," \nLast Name: ", "\t",  employee_name[10:16])
print("\n")

chief_technology_officer_name = 'Carter_Smith'
print(chief_technology_officer_name.rjust(10))
print("\n")
print(chief_technology_officer_name.rjust(20))
print("\n")
print(chief_technology_officer_name.center(20, "="))
print("\n")


spam = '     McGill     '
print(spam.strip(), "<<< with cursor")
print(spam.lstrip(), "<<< with cursor")
print(spam.rstrip(), "<<< with cursor")



