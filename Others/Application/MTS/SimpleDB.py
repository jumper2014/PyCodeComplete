# coding=utf-8
# author = ZengYueTian
# date = 2015-04-01

from tornado.options import define, options
import torndb

define("mysql_host", default="192.168.199.110:3306", help="database host")
define("mysql_database", default="morbot", help="database name")
define("mysql_user", default="root", help="database user")
define("mysql_password", default="123456", help="database password")

class SimpleDB(object):
    db = None
    def __init__(self):
        self.db = torndb.Connection(
                host=options.mysql_host, database=options.mysql_database,
                user=options.mysql_user, password=options.mysql_password)



    def INSERT_USER(self, name, hashed_password):
        query_sql = "insert into user(name, hashed_password) values( %s, %s)"
        raw_data = self.db.insert(query_sql, name, hashed_password)
        return raw_data




    def GET_USER_COUNT(self):
        query_sql = "select count(*) from user"
        raw_data = self.db.query(query_sql)
        return raw_data

    def GET_USER_BY_NAME(self, name):
        query_sql = "select * from user where name = '" + name + "'"
        raw_data = self.db.query(query_sql)
        return raw_data



    def GET_USER_BY_ID(self, user_id):
        query_sql = "select * from user where id = '" + user_id + "'"
        raw_data = self.db.query(query_sql)
        return raw_data


    def GET_USERID_BY_NAME(self, user):
        query_sql = "select id from user where name="+"'" + user + "'"
        raw_data = self.db.query(query_sql)
        return raw_data


    def GET_TESTCASE_ID_BY_USER_AND_CASE(self, user, case):
        query_sql = "select testcase.id from testcase, user where testcase.user=user.id and user.name=" \
                    +"'"+user+"' and tc_id='" + case +"'"
        raw_data = self.db.query(query_sql)
        return raw_data

    def GET_TESTCASE_BY_USER(self, user):
        query_sql = "select * from testcase, user where testcase.user=user.id and user.name="+"'"+user+"'"
        raw_data = self.db.query(query_sql)
        return raw_data

    def GET_TESTCASE_BY_STATUS(self, status):
        query_sql = "select * from testcase where status like '%%" + status + "%%'"
        raw_data = self.db.query(query_sql)
        return raw_data

    def INSERT_TESTCASE(self, tc_id, script_file, user):
        query_sql = "insert into " \
                    "testcase(tc_id, script_file, user) " \
                    "values(%s, %s, %s)"
        raw_data = self.db.insert(query_sql, tc_id, script_file, user)
        return raw_data

    def INSERT_TASK(self, tc_id, device_id, status):
        query_sql = "insert into " \
                    "task(tc_id, device_id, status) " \
                    "values(%s, %s, %s)"
        raw_data = self.db.insert(query_sql, tc_id, device_id, status)
        return raw_data

    def GET_TASK_BY_USER(self, user):
        query_sql = "select testcase.tc_id, task.status, device.os, device.mode "  \
        "from task, user, testcase, device where testcase.user=user.id " \
        "and user.name='" + user + "'" + " and task.tc_id=testcase.id and device.id=task.device_id"

        raw_data = self.db.query(query_sql)
        return raw_data

    def UPDATE_TASK(self, task_id, status):
        query_sql = "update task set status='" + status + "' where id="+task_id
        print query_sql
        raw_data = self.db.execute(query_sql)
        return raw_data

    def UPDATE_TASK_TO_SUBMIT(self):
        query_sql = "update task set status='submit'"
        print query_sql
        raw_data = self.db.execute(query_sql)
        return raw_data


    def GET_TASK_BY_STATUS(self, status):
        query_sql = "select task.id, testcase.script_file, robot.ip "  \
        "from task, testcase, robot where task.status='"+ status+ "'" \
        " and task.tc_id=testcase.id and robot.device_id=task.device_id"

        raw_data = self.db.query(query_sql)
        return raw_data

    def GET_DEVICE(self, ):
        query_sql = "select * from device"
        raw_data = self.db.query(query_sql)
        return raw_data

    def GET_DEVICE_ID(self, os, mode):
        query_sql = "select id from device where os = '" + os + "'" + " and mode='" + mode +"'"
        raw_data = self.db.query(query_sql)
        return raw_data

