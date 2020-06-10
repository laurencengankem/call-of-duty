import pika
import time
import json
from pymongo import MongoClient

username='sarapizzz'

data=''
with open('sara.json') as json_file:
    data = json.load(json_file)

client = MongoClient('localhost', 27017)
db = client['instadb']
collection_profile = db['profiledb']

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='task_queue', durable=True)

def test_parser_process():
    collection_profile.delete_many({"username":username})
    time.sleep(2)
    channel.basic_publish(exchange='',
                  routing_key='task_queue',
                  body=json.dumps(data),
                  properties=pika.BasicProperties(delivery_mode=2,))
    time.sleep(2)
    pr=list(collection_profile.find({'username':username}))
    try:
        pr=pr[0]
    except:
        print(pr)
    assert pr['username']==username
    assert pr['n_followers']== "296"
    assert pr["n_following"]=="919"
    assert pr["n_post"]== 4
