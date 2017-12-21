"""
launch.py
Copyright (c) 2017 andynines
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
    logger.initialize()
    logger.log("Automail launched\nPress Ctrl+C to terminate bot")
    try:
        while True:
            current_hour = datetime.datetime.now().hour
            if (current_hour == settings.SEND_HOUR) and ready:
                bot.routine()
                ready = False
            elif (current_hour == (settings.SEND_HOUR + 1) % 24) and not ready:
                ready = True
            time.sleep(settings.SLEEP_TIME)
    except KeyboardInterrupt:
        logger.log("\nBot terminated")

if __name__ == "__main__":
    main()
