"""
initialize.py
Copyright (c) 2018 andynines
MIT License
"""

import compose, logger

def main():
    """
    Initialize the environment before the launch of a new automail bot.
    """
    logger.initialize()
    compose.set_previous(0)
    
if __name__ == "__main__":
    main()
