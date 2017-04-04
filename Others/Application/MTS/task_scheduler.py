# coding=utf-8
# author = ZengYueTian
# date = 2015-04-01

#
# Description:  test task schedule workflow
#

from Scheduler import *
import time


if __name__ == "__main__":

    scheduler = Scheduler()
    scheduler.clean_redis_db()
    scheduler.reset_task_to_submit()

    while True:
        time.sleep(1)
        scheduler.get_robot_status()

        time.sleep(1)
        scheduler.get_task_status()

        time.sleep(1)
        scheduler.sync_submitted_task()

        time.sleep(1)
        scheduler.schedule_task()

        time.sleep(3)






