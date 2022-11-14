'''

https://github.com/jhnwr/whiskey-cronjob/blob/main/new-whisky.py
refrence 
https://saqibameen.com/blog/deploy-python-cron-job-scripts-on-heroku
'''

from datetime import datetime

def cronjob():
    """
    Main cron job.
    The main cronjob to be run continuously.
    """
    print("Cron job is running")
    print("Tick! The time is: %s" % datetime.now())

