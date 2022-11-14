'''
pip install APScheduler

pip install pipenv
'''

# Package Scheduler.
from apscheduler.schedulers.blocking import BlockingScheduler

# Main cronjob function.
from main import cronjob

# Create an instance of scheduler and add function.
scheduler = BlockingScheduler()
scheduler.add_job(cronjob, "interval", seconds=30)

scheduler.start()


'''

# Run.
$ python cronjob.py
# Cron job is running
# Tick! The time is: 2019-09-23 01:54:15.210989
'''