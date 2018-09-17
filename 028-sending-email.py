###############################################################################
# Sending email 
###############################################################################

import smtplib

smtpObj = smtplib.SMTP('smtp.zoho.com', 465)

smtpObj.ehlo()

smtpObj.starttls()

smtpObj.login('jdanson@zoho.com', 'xxxxxxxxxxxxxx')

smtpObj.sendmail('jdanson@zoho.com', 'johndanson@icloud.com', 'Subject: x.\nDear Dominique, x, John')

smtpObj.quit()

