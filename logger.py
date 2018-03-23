"""
logger.py
Copyright (c) 2018 andynines
MIT License
"""

import settings
import datetime, sys

def log(text, newline=True, warn=False):
    """
    Recieves text as input that will be logged in the designated file as well as
    printed to stdout.
    """
    assert type(text) is str
    message = str(datetime.datetime.now()) + " " 
    message += ("WARNING: " if warn else "")
    message += text
    message += ("\n" if newline else "")
    with open(settings.LOG, "a") as file:
        file.write(message)
    sys.stdout.write(message)
    
def initialize():
    """
    Creates a new log. Should be called before any other log operations.
    """
    with open(settings.LOG, "w"):
        pass
    log("Fresh log")
    
def tidy():
    """
    Clean the file by keeping it within the maximum number of lines permitted.
    This is achieved by reading the entire file, then truncating it and only
    writing back the most recent lines.
    """
    log("Tidying up log")
    with open(settings.LOG, "r") as file:
        lines = file.readlines()
    length = len(lines) + 1 #offset log entires created by this function
    if length > settings.MAX_LINES:
        with open(settings.LOG, "w") as file:
            for line in lines[length - settings.MAX_LINES:]:
                file.write(line)
        log("Log cleaned")
    else:
        log("Log already clean")
