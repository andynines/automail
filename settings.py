"""
settings.py
Copyright (c) 2017 andynines
MIT License
"""

import os

USERNAME = "myemail@provider.com" #email address from which the messages are sent
PASSWORD = "mypassword" #the email account's respective password
HOST = "smtp.provider.com" #smtp server domain name
PORT = 587 #port number to connect to
SSL = False #connect to SMTP server with SSL encryption
TLS = True #use TLS encryption when sending emails

RECIPIENTS = os.path.join("records", "recipients.txt") #path to list of recipients' addresses
SUBJECT = "Your Daily Quote has Arrived" #string to appear in subject of each email
CONTENT = os.path.join("records", "content.txt") #path to content file to pull material from
MESSAGE = os.path.join("records", "message.txt") #path to file where possible server messages are stored
END_MESSAGE = "Have a nice day!" #message that appears at the end of emails

LOG = os.path.join("records", "log.txt") #path to file which logger will write and manage
MAX_LINES = 200 #maximum number of lines before the logger begins to delete old entries

SEND_INTERVAL = 24 #how many hours between routines
SLEEP_TIME = 5 #how many seconds between time checks during standby