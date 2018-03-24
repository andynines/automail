"""
compose.py
Copyright (c) 2018 andynines
MIT License
"""

import logger, settings
import math, random

def get_previous(read_bytes):
    """
    Retrieve the index of the last selection to appear in an email.
    """
    with open(settings.PREVIOUS, "r") as file:
        index = int(file.read(read_bytes))
    return index
    
def set_previous(index):
    """
    Set an index to not be a possible selection for the next piece of content.
    """
    with open(settings.PREVIOUS, "w") as file:
        file.write(str(index))

def daily_selection():
    """
    Select a random piece of material from what is available. A piece is defined
    by a newline; every line is a new piece of content.
    """
    logger.log("Selecting today's material")
    with open(settings.CONTENT, "r") as file:
        content = file.readlines()
    lines = len(content)
    prev = get_previous(int(math.log10(lines)))
    selection_index = random.choice(list(range(prev)) + list(range(prev + 1, lines)))
    selection = content[selection_index]
    selection += ("\n" if selection[-1] != "\n" else "")
    logger.log("Selected: " + selection, newline=False)
    set_previous(selection_index)
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
