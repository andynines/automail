"""
settings.py
Copyright (c) 2017 andynines
MIT License
"""

import os

#connection settings
USERNAME = "myemail@provider.com" #email address from which the messages are sent
PASSWORD = "mypassword" #the email account's respective password
HOST = "smtp.provider.com" #smtp server domain name
PORT = 555  #port number to connect to
SSL = False #connect to SMTP server with SSL encryption
TLS = True #use TLS encryption when sending emails

#message settings
RECIPIENTS = ["buddy@provider.com", #recipients' email addresses
              "anotherrecipient@anotherprovider.com",
              "lastexample@lastprovider.com"]
SUBJECT = "Your daily quote has arrived" #string to appear in subject of each email
CONTENT = os.path.join("records", "quotes.txt") #path to content file to pull material from
END_MESSAGE = "Have a nice day!" #message that appears at the end of emails
URL = "https://www.github.com/andynines/automail" #link to the github repo

#log settings
LOG = os.path.join("records", "log.txt") #path to file which logger will write and manage
MAX_LINES = 300 #maximum number of lines before the logger begins to delete old entries

#timer settings
SEND_HOURS = [7] #hours at which emails are sent daily; use 24-hour clock
SLEEP_TIME = 1800 #second interval between time checks
