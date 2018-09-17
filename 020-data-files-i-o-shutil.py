###############################################################################
# SHUTIL Data files i/o
###############################################################################

# using SHUTIL used to move files around your directory file system... observe references at the top!

import os
import shutil

os.mkdir("c:\python\examples")
shutil.copy("c:\python\profile0.txt", "c:\python\examples")
myfiles = os.listdir("c:\python\examples")
print(myfiles)
os.remove("c:\python\profile0.txt")

# os.rmdir("c:\python\examples") <<< would remove the result...




