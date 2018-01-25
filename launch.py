"""
launch.py
Copyright (c) 2018 andynines
MIT License
"""

import bot, logger, settings
import datetime, time

def main():
    """
    Initializes the environment for a new automail bot, and schedules it to run
    when specified in the settings module.
    """
    ready = True
    prev_hour = None
    logger.initialize()
    logger.log("Automail launched\nPress Ctrl+C to terminate bot")
    try:
        while True:
            current_hour = datetime.datetime.now().minute #hour
            if (current_hour in settings.SEND_HOURS) and ready:
                logger.log("Beginning operations for hour " + str(current_hour))
                bot.routine()
                ready = False
                prev_hour = current_hour
                logger.log("Ending operations for hour " + str(current_hour))
            elif (current_hour != prev_hour) and not ready:
                ready = True
            time.sleep(settings.SLEEP_TIME)
    except KeyboardInterrupt:
        logger.log("\nBot terminated")

if __name__ == "__main__":
    main()
