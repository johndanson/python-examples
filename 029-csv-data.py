###############################################################################
# CSV
###############################################################################

import csv

exampleFile = open('c:\python\example.csv')

# Read the CSV file in (skipping first row).
csvRows = []
csvFileObj = open('c:\python\example.csv')
readerObj = csv.reader(csvFileObj)
for row in readerObj:
    if readerObj.line_num == 1:
        continue    # skip first row
    print(row)
csvFileObj.close()

