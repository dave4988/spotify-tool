# spotify-tool
A tool that follows all artists and likes all albums of songs you have liked on spotify

To use, be sure you have Python 3 installed and run spotify-tool.py from the command line. Arguments are --client-id and --client-secret, which you can obtain from the spotify Application page (make a new app and you'll get an id and secret).

Authentication to your account is a little clunky right now, when you run the program you'll have a browser open and be requested to login, then you'll have to paste the URL back into the command line. Next step is to throw a thin web layer on top of the script to make this less cludgy.
