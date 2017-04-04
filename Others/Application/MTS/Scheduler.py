# coding=utf-8
# author = ZengYueTian
# date = 2015-04-01

import string
import redis

from SimpleDB import *
from Request import *


# class responsible for task scheduling
class Scheduler(object):

    # const goes here
    redis_port = 6379
    robot_port = "8011"
    ready_robot = 1
    scheduled_robot = 2
    submitted_task = 6
    scheduled_task = 7

    task_script = 9

    rdb_ready_robot = None
    rdb_submitted_task = None
    rdb_scheduled_task = None
    rdb_scheduled_robot = None
    rdb_task_script = None
    rdb_list = []
    db = None

    # constructor
    def __init__(self):
        self.db = SimpleDB()
        self.rdb_ready_robot = redis.Redis(port=self.redis_port, db=self.ready_robot)
        self.rdb_submitted_task = redis.Redis(port=self.redis_port, db=self.submitted_task)
        self.rdb_scheduled_task = redis.Redis(port=self.redis_port, db=self.scheduled_task)
        self.rdb_scheduled_robot = redis.Redis(port=self.redis_port, db=self.scheduled_robot)
        self.rdb_task_script = redis.Redis(port=self.redis_port, db=self.task_script)
        self.rdb_list = [self.rdb_ready_robot, self.rdb_submitted_task, self.rdb_scheduled_task,
                         self.rdb_scheduled_robot, self.rdb_task_script]
        print "Init done"

    # set mysql task table to make all task "submit" status
    def reset_task_to_submit(self):
        self.db.UPDATE_TASK_TO_SUBMIT()



    # delete all data in redis database
    def clean_redis_db(self):
        for rdb in self.rdb_list:
            rdb.flushdb()

    # check robots' status, and place ready robot to redis table
    def get_robot_status(self):
        print "\n             Start scanning robot\n"
        self.rdb_ready_robot["1"] = "192.168.199.172"
        # get all robots
        robot_list = self.rdb_ready_robot.keys()
        for robot in robot_list:
            robot_ip = self.rdb_ready_robot[robot]
            uri_robot_status = self.create_uri_for_robot_status(robot_ip)
            # GET robot's status
            robot_status = YZZ_REQUEST(uri_robot_status, 'GET')
            print "Robot %(ip)s is %(status)s " % {'ip': robot_ip, 'status': robot_status}

    # get and update task status
    def get_task_status(self):
        print "\n             Start getting task result\n"
        scheduled_task_list = self.rdb_scheduled_task.keys()
        for task_id in scheduled_task_list:
            robot_ip = self.rdb_scheduled_task[task_id]
            uri_robot_task = self.create_uri_for_task_status(robot_ip, task_id)
            print uri_robot_task
            status = YZZ_REQUEST(uri_robot_task, 'GET')
            if status != 'running':
                # update redis on server
                self.rdb_task_script.delete(task_id)
                self.rdb_scheduled_task.delete(task_id)
                # delete task on robot
                YZZ_REQUEST(uri_robot_task, 'DELETE')
                self.rdb_scheduled_robot.delete(robot_ip)
                # write back to db
                print "Task " + task_id + " status is " + status
                self.db.UPDATE_TASK(task_id, status)


            else:  # still running, do nothing
                pass

    # sync submitted task for redis and mysql
    def sync_submitted_task(self):
        print "\n             Start sync task\n"
        submitted_tasks = self.db.GET_TASK_BY_STATUS("submit")
        for task in submitted_tasks:
            task_id = str(task["id"])
            script_file = task["script_file"]
            if not(self.rdb_submitted_task.exists(task_id)) and not(self.rdb_scheduled_task.exists(task_id)):
                self.rdb_submitted_task[task_id] = script_file
                self.rdb_task_script[task_id] = script_file


    # update schedule redis table
    def schedule_task(self):
        print "\n             Start schedule task\n"
        # get robot
        robot_ip = self.rdb_ready_robot["1"]

        # get submitted task list from redis
        task_list = self.rdb_submitted_task.keys()
        task_id_list = map(string.atoi, task_list)
        task_id_list.sort()
        task_id_list = map(str, task_id_list)
        print "Submitted Task list -> ", task_id_list

        # schedule task to robot without task running
        for task_id in task_id_list:
            if not self.rdb_scheduled_robot.exists(robot_ip):
                # move the task from submitted list to scheduled list
                self.rdb_scheduled_task[task_id] = robot_ip
                self.db.UPDATE_TASK(task_id, "scheduled")
                self.rdb_submitted_task.delete(task_id)

                # add the task to robot list
                self.rdb_scheduled_robot[robot_ip] = task_id
                self.dispatch_task(task_id, robot_ip)
                print "Robot " + robot_ip + " will run task " + task_id
            else:
                print "Robot " + robot_ip + " has task " + self.rdb_scheduled_robot[robot_ip] \
                      + " , wait it finish."
        # print scheduled tasks
        scheduled_task_list = self.rdb_scheduled_task.keys()
        print "Scheduled Task List -> ", scheduled_task_list

    # dispatch json task to robot
    def dispatch_task(self, task_id, robot_ip):
        uri_robot_task = self.create_uri_for_task_status(robot_ip, task_id)
        script_file = "uploads/" + self.rdb_task_script[task_id]
        test_step_list = self.transfer_case_to_json(script_file)
        print test_step_list
        # create new task on robot
        result = YZZ_REQUEST(uri_robot_task, 'POST', test_step_list)
        print "Task dispatch result is " + result
        # update task status to scheduled
        print "Task " + task_id +"was scheduled to " + robot_ip

    # to format uri
    def create_uri_for_robot_status(self, robot_ip):
        uri = "http://%(ip)s:%(port)s/host/status" % {'ip': robot_ip, 'port': self.robot_port}
        return uri

    # to format uri
    def create_uri_for_task_status(self, robot_ip, task_id):
        uri = "http://%(ip)s:%(port)s/task/%(task_id)s" % {'ip': robot_ip, 'port': self.robot_port, 'task_id': task_id}
        return uri

    # transfer case content to list (line by line)
    def transfer_case_to_json(self, case_file):
        test_step_list = []
        file_object = open(case_file)
        try:
            for line in file_object:
                line = line.strip()
                word_list = line.split()
                test_step_list.append({"action": word_list[0], "object": word_list[1]})
        finally:
            file_object.close()
        # transfer to json format
        return test_step_list




















