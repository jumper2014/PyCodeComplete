# coding=utf-8

from celery import Celery

broker = 'redis://127.0.0.1:6379/5'
backend = 'redis://127.0.0.1:6379/6'

app = Celery('tasks', broker=broker, backend=backend)


@app.task
def add(x, y):
    return x+y




