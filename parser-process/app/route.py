import pika
import time
import json
from pymongo import MongoClient
from app.parser import get_profile
from app.parser import get_comment
from app.parser import get_post
from app.parser import profiling
from app import app
from flask import request
from app.parser.get_sentiment_analysis import get_comment as gc


'''
    This function open a connection with MongoDB and waits from the queue until an JSON is found. Then it processes it
    and insert the result into the db
'''

i = 0
j = 0
n = 0

@app.route('/', methods=['POST'])
def listen_to_username():
    #client = MongoClient('mongodb://admin:admin@10.200.1.67/instadb', 27017)
    #client = MongoClient('localhost', 27017)
    client = MongoClient('3.223.148.248', 27017)
    db = client['instadb']
    collection_profile= db['profiledb']
    collection_comment=db['commentdb']

    global i
    global j
    global n
    try:
        message = request.get_json()

        if message.get('logging_page_id') is not None:
            context = get_profile.get_user_data(message)
            collection_profile.insert_one(context)
            'reset post_profile lists '
            profiling.reset_profile_post()
            profiling.reset_profile_post_1()

        elif message.get('data', {}).get('user') != None:
            print(" [*] START POST")

        elif message.get('data', {}).get('shortcode_media') != None:
            print(" [*] START COMMENT")
            context_comment = get_comment.get_comment_data(message)
            comment_has_next_page = profiling.get_comment_has_next_page(message)
            j = j + 1
            if not comment_has_next_page or j == 3:
                collection_comment.insert_one(context_comment)
                'reset comment lists '
                profiling.reset_comment()
                reset_i_j()
        time.sleep(0.2)
        return "Made",200
    except:
        return "problem", 404




@app.route('/sentiment', methods=['POST'])
def sentiment_analysis():
    data = request.data
    sentiment = gc(data)
    return sentiment


def reset_i_j():
    global i
    global j
    i = 0
    j = 0

def reset_n():
    global n
    n = 0
