"""
compose.py
Copyright (c) 2017 andynines
MIT License
"""

import logger, random, settings

prev = None

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
    logger.log("Selected: " + selection, newline=False)
    return selection

def owner_message():
    """
    Checks whether the owner has prepared a message for the next round of
    emails. All contents of the message file will be sent as that day's
    message, and its contents will be deleted. If the file is empty, the emails
    are sent with no message.
    """
    logger.log("Checking for message")
    with open(settings.MESSAGE, "r") as file:
        text = "".join(file.readlines())
    logger.log(("Message: " + text)
               if text else
               "No message found\n", newline=False)
    with open(settings.MESSAGE, "w") as file:
        pass
    logger.log("Message file cleaned")
    return text

def message():
    """
    Returns a message string that is ready to be placed into the final email.
    Will follow the format:
    Subject: [subject text]\n
    [email text]\n
    \n [if message follows]
    [a message if the owner intends to send one]
    \n [if there was a message]
    [end message]
    """
    logger.log("Organizing message")
    current_message = owner_message()
    final = ("Subject: " + settings.SUBJECT + "\n" +
            daily_selection() + "\n" +
            (("MESSAGE: " + current_message + "\n") if current_message else "") +
             settings.END_MESSAGE)
    logger.log("Begin final message:\n" + final + "\nEnd final message")
    return final
