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
    as specified in the settings module.
    """
    logger.initialize()
    logger.log("New automail bot initialized")
    send_interval = settings.SEND_INTERVAL
    sleep_time = settings.SLEEP_TIME
    while True:
        bot.routine()
        current_dt = datetime.datetime.now()
        logger.log("Going on standby at {}.{}.{}.{}.{}.{}".format(current_dt.year,
                                                                  current_dt.month,
                                                                  current_dt.day,
                                                                  current_dt.hour,
                                                                  current_dt.minute,
                                                                  current_dt.second))
        next_dt = current_dt + datetime.timedelta(hours=send_interval)
        while datetime.datetime.now() < next_dt:
            time.sleep(sleep_time)

if __name__ == "__main__":
    main()
