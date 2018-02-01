# Automail
Automail is an email bot that sends out selections from a content file during specified hours of the day. It's perfect for something like a "daily quote" mailing list, or anything else that you can imagine!
## License
The contents of this repository are made available under the MIT License.
## Setup
Open settings.py to configure a new bot. Automail cannot work properly until it is given the parameters to properly connect to a valid email account. Run launch.py to activate the bot. The composer looks at each individual line of the content file as a possible selection.
## Sample email
    Subject: Your daily quote has arrived
    "Every time we open our mouths, people can look into our minds."

    Have a nice day!
    Fork me on GitHub: https://www.github.com/andynines/automail
