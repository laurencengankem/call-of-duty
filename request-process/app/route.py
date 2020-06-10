from app import start
import pika
import time
from app import app

'''
    Open a connection to localhost using pika client and wait for a message from the username_queue, that returns
    the username to be searched
'''

@app.route('/<username>')
def listen_to_username(username):
    print(" [x] Done")
    start.request_to_username(username)
    return "recived" , 200
