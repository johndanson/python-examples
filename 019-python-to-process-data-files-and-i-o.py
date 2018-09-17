###############################################################################
# Python to process data files and i/o read lines, red+write etc, SHUTIL..
###############################################################################


# read lines
f = open("c:\python\profile1.txt", "r")
for lines in f:
    print(lines)
f.close()

print("The file is closed")


# read from file 1 ... write lines to file 0
infile = open("c:\python\profile1.txt", "r")
outfile = open("c:\python\profile0.txt", "w")
for line in infile:
    print(line, file=outfile)
    print("The copy operation is done")
infile.close()
outfile.close()
print("The files are closed")




