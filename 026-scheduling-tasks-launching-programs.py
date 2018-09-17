###############################################################################
# Scheduling tasks and launching programs
###############################################################################

import time
import subprocess


def calcprod():
    # Calculate the product of the first 100,000 numbers.
    product = 1
    for ix in range(1, 15000):
        product = product * ix
    return product


startTime = time.time()
prod = calcprod()
endTime = time.time()
print('The result is %s digits long.' % (len(str(prod))))
print('Took %s seconds to calculate.' % (endTime - startTime))


# timing by 1 second, pause by one second
for i in range(3):
    print('Tick')
    time.sleep(1)
    print('Tock')
    time.sleep(1)
time.sleep(5)


# Create and start the Thread objects.
calcproc = subprocess.Popen('c:\\Windows\\System32\\calc.exe')
calcproc.wait()
calcproc.poll()

# Running Other Python Scripts
subprocess.Popen(['C:\\python34\\python.exe', '018-regex.py'])

