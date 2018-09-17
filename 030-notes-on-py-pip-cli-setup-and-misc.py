###############################################################################
# Running python from the command line, and pyautogui.
###############################################################################


# Windows        #! py -3 [filename.py]

# Mac            #! /usr/bin/env python3.

# Linux          #! /usr/bin/python3.

###############################################################################
# Installing third party modules, pip as standard n py3.4 onwards
###############################################################################

# ensure pip is up to date             python -m pip install --upgrade pip
# pip install pyautogui

# (or pip3 install –U ModuleName on OS X and Linux).

###############################################################################
# PyAutoGui
###############################################################################

# To install - on Windows, nothing to do - all done

# On OS X, run sudo pip3 install pyobjc-framework-Quartz,
# sudo pip3 install pyobjc-core, and then sudo pip3 install pyobjc.

# On Linux, run sudo pip3 install python3-xlib, sudo apt-get install scrot,
# sudo apt-get install python3-tk, and sudo apt-get install python3-dev.
# (Scrot is a screenshot program that PyAutoGUI uses.)

# Pauses...Size...MouseMove...Get-Position...

import pyautogui

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

# pyautogui.size()(1920, 1080)
# width, height = pyautogui.size()

# for i in range(10):
#       pyautogui.moveTo(100, 100, duration=0.25)
#       pyautogui.moveTo(200, 100, duration=0.25)

# pyautogui.position()(311, 622)

# im = pyautogui.screenshot()

pyautogui.click(100, 100)
pyautogui.typewrite('D McGill!')





