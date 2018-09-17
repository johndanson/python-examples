###############################################################################
# Regex example, my phone number and the old cell number....
###############################################################################


def isphonenumber(text):

    if len(text) != 12:
            return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
            return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True


message = 'Call me when you like, Dominique - 442-216-9318 no longer works, but my new cell 760-917-2847 is good.'
for j in range(len(message)):
    chunk = message[j:j+12]
    if isphonenumber(chunk):
        print('Phone number found: ' + chunk)
print('Done')


