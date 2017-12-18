"""
bot.py
Copyright (c) 2017 andynines
MIT License
"""

import compose, logger, settings
import smtplib

def failure(warning):
    logger.log(warning, warn=True)
    return False

def routine():
    """
    Executes the bot's routine operations.
    """
    logger.tidy()
    logger.log("Beginning operations")
    message = compose.message()
    logger.log("Initializing SMTP object")
    smtp = (smtplib.SMTP_SSL(settings.HOST, settings.PORT)
            if settings.SSL else
            smtplib.SMTP(settings.HOST, settings.PORT))
    logger.log("Saying 'hello' to server")
    if not smtp.ehlo()[0] == 250:
        return failure("Server greeting failed")
    if settings.TLS:
        logger.log("Initializing TLS encryption")
        if not (smtp.starttls()[0] == 220):
            return failure("TLS initialization failed")
    logger.log("Logging in")
    if not (smtp.login(settings.USERNAME, settings.PASSWORD)[0] == 235):
        return failure("Login failed")
    logger.log("Sending emails")
    send_results = smtp.sendmail(settings.USERNAME,
                                 settings.RECIPIENTS,
                                 message)
    if not (send_results == {}):
        logger.log("Sending failed for the following recipients: ", warn=True)
        for address in send_results.keys():
            logger.log(" - ".join([str(element) for element in send_results[address]]))
    logger.log("Logging out")
    smtp.quit()
    logger.log("Operations complete")
