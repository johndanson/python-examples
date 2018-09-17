##############################################################################
# Flow control statements  if ... if-else ... if elif elif else
##############################################################################

MMG = 10
y = 3
if MMG > y:
    print("MMG is greater than y")

MMG = 10
y = 3
if MMG < y:
    print("MMG is greater than y")
else:
    print("Y is not greater than MMG")

MMG = 12
y = 3
z = 102

if MMG < y:
    print("x is greater than y")
elif y == MMG:
    print("y is not greater than x")
elif z == MMG:
    print("z is equal to x")
else:
    print("none of the above are as good as MMG")

