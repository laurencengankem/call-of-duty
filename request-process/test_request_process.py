import pika
import time
import json
import requests
from urllib import parse

name=""
username="cristiano"

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel2= connection.channel()
channel.queue_declare(queue='username_queue', durable=True)
channel2.queue_declare(queue='task_queue', durable=True)

def callback(ch, method, properties, body):
    time.sleep(0.2)
    msg= json.loads(body)
    try:
        global name
        name= msg['graphql']['user']['username']
        ch.basic_ack(delivery_tag=method.delivery_tag)
        connection.close()
    except:
        ch.basic_ack(delivery_tag=method.delivery_tag)


''' This functional test  checks if the service request-process coorectly listen to the username_queue, make  requestd to
     the instagram API for the usernames contained inside  and publish the responses inside the task_queue
'''

def test_request_process():
    channel.basic_publish(exchange='',
                      routing_key='username_queue',
                      body=username,
                      properties=pika.BasicProperties(delivery_mode=2,))
    time.sleep(1)
    t0 = time.time()
    t0= t0+60
    while name != username and time.time()< t0 :
        channel2.basic_qos(prefetch_count=1)
        channel2.basic_consume(queue='task_queue', on_message_callback=callback)
        channel2.start_consuming()
    assert name == username
