# Automail
Automail is an email bot built to regularly send out selections from a content file to a group of recipients. Out of the box, it's built to function as a daily quotes mailing list.
## License
The contents of this repository are made available under the MIT License.
## Setup
Setting up an Automail bot is fast and simple.
1. **Gather material for the content file.** By default, the content file is located in the `records` folder and is called `quotes.txt`. The composer views each individual line of this file as a possible selection to appear in an email.
2. **Configure a new bot.** The constants which will be used to log into an email account and style the message are declared in `settings.py`. Your email provider determines what server domain name and port number to use, and may require you to undergo additional steps before you may log into an account programatically.
3. **Initialize the environment.** Move your current directory to the top level of the repository and run `initialize.py`.
4. **Schedule the bot.** Using Windows Task Scheduler or Cron, schedule `automail.py` to run whenever you desire. It will be completely self-sufficient from hereon.
## Usage
### Log dump
The bot actively logs all of its actions.

    2018-03-23 23:20:03.167494 Fresh log
    2018-03-23 23:20:28.217927 Beginning new mail cycle
    2018-03-23 23:20:28.218927 Tidying up log
    2018-03-23 23:20:28.229928 Log already clean
    2018-03-23 23:20:28.230928 Organizing message
    2018-03-23 23:20:28.236928 Selecting today's material
    2018-03-23 23:20:28.238928 Selected: "Every time we open our mouths, people can look into our minds."
    2018-03-23 23:20:28.239928 Begin final message:
    Subject: Your daily quote has arrived
    "Every time we open our mouths, people can look into our minds."

    Have a nice day!
    Fork me on GitHub: https://www.github.com/andynines/automail
    End final message
    2018-03-23 23:20:28.241928 Initializing SMTP object
    2018-03-23 23:20:28.473942 Saying 'hello' to server
    2018-03-23 23:20:28.521944 Initializing TLS encryption
    2018-03-23 23:20:29.230985 Logging in
    2018-03-23 23:20:29.393994 Sending emails
    2018-03-23 23:20:29.948026 Logging out
    2018-03-23 23:20:29.979028 Terminating mail cycle
### Email
Messages appear to recipients like the following.

    Subject: Your daily quote has arrived
    "Every time we open our mouths, people can look into our minds."

    Have a nice day!
    Fork me on GitHub: https://www.github.com/andynines/automail
