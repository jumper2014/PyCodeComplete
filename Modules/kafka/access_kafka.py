# coding=utf-8
from pykafka import KafkaClient

import codecs
import logging

logging.basicConfig(level=logging.INFO)


# create kafka data, string format
def produce_kafka_data(kafka_topic):
    with kafka_topic.get_sync_producer() as producer:
        for i in range(4):
            producer.produce('test message ' + str(i ** 2))


# consume data
def consume_simple_kafka(kafka_topic, timeout):
    consumer = kafka_topic.get_simple_consumer(consumer_timeout_ms=timeout)
    for message in consumer:
        if message is not None:
            print message.offset, message.value

client = KafkaClient(hosts = "192.168.253.147:6667")
topic = client.topics["test"]
produce_kafka_data(topic)
consumer = topic.get_simple_consumer(consumer_timeout_ms=1000)
cnt = 0
for message in consumer:
    if message is not None:
        print message.offset, message.value
    cnt += 1
print cnt
