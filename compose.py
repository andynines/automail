"""
compose.py
Copyright (c) 2017 andynines
MIT License
"""

import logger, settings
import random

prev = None #store previous quote to prevent repeats

def daily_selection():
    """
    Select a random piece of material from what is available. A piece is defined
    by a newline; every line is a new piece of content.
    """
    logger.log("Selecting today's material")
    with open(settings.CONTENT, "r") as file:
        lines = file.readlines()
    selection = (random.choice(lines[0:prev] + lines[prev + 1:])
                 if prev else
                 random.choice(lines))
    selection += ("\n" if selection[-1] != "\n" else "")
    logger.log("Selected: " + selection, newline=False)
    return selection

def message():
    """
    Returns a message string that is ready to be placed into the final email.
    """
    logger.log("Organizing message")
    final = ("Subject: " + settings.SUBJECT + "\n" +
             daily_selection() + "\n" +
             settings.END_MESSAGE + "\n" +
             "Fork me on GitHub: " + settings.URL)
    logger.log("Begin final message:\n" + final + "\nEnd final message")
    return final
