readme.txt

About
---
Automail is a periodic email bot for mailing lists that send out things like
quotes, jokes, and facts.

License
---
The contents of this repository are made available under the MIT License.

Use
---
1. Prepare an email account for the bot to send messages with.
2. Enter the account's information in settings.py, and set any other options.
3. In records/recipients.txt, enter the recipients of the emails, one per line.
4. Paste the email content into records/content.txt. Every line should be an
independent piece of material. For instance, in a quote mailing list, every line
of records/content.txt should contain a new quote.
5. Optionally, enter a message to be contained only within the next email inside
records/message.txt. End it with a newline.
6. Run launch.py.

A random piece of content from records/content.txt, along with any message in
records/message.txt, will be sent out to each email address in
records/recipients.txt. All output will be printed as well as stored inside
recipients/log.txt.
