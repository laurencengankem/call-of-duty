from app import app
from app import start
from app import search_stat
from pymongo import MongoClient
import json
from bson import json_util
import time
import click
from datetime import date
from flask_cors import CORS
from bson import json_util
import requests

'''
    Open connection to mongodb, using "instadb" as database and "profiledb" as collection. Verify that you have
    correctly installed MongoDB and created the database and collection
'''
#client = MongoClient('mongodb://admin:admin@10.200.1.67/instadb', 27017)
client = MongoClient('localhost', 27017)
db = client['instadb']
collection_profile = db['profiledb']
collection_comment = db['commentdb']
current_date = date.today()

'''
    If false it doesn't send any requests and used pre-cached JSON
'''
flag = True

'''
    Whenever is sent a request to this server at the address '/s/<username>', hello function publishes into the queue
    the username provided. Then it queries the db asking for the relative json. Whenever that JSON has not yet been
    produced, it tries again after a few seconds.
'''
@app.route("/s/<username>")
def hello(username):
    query = {'username': username}
    '''
        At first, it searched for the JSON of the username and, if found, doesn't send any more requests
    '''
    try:
        context = list(collection_profile.find(query))[-1]
        profile_date = context['date_time']
        if current_date.strftime('%d') == profile_date.strftime('%d') \
                and profile_date.strftime('%m') == profile_date.strftime('%m'):
            js = json.dumps(context, indent=4, default=json_util.default)
            click.secho(
                "\n [route.py]\t\tA recently downloaded JSON was found, no further requests will be sent",
                fg="green",
            )
            search_stat.new_search(username)
            return js
        else:
            click.secho(
                "\n [route.py]\t\tThe cached JSON is too old, wait for the new JSON to be downloaded",
                fg="green",
            )
            r = requests.get("http://127.0.0.1:5001/"+username)
            #time.sleep(5)
            if r.status_code==200:
                context = list(collection_profile.find(query))[-1]
                profile_date = context['date_time']
                if current_date.strftime('%d') == profile_date.strftime('%d') \
                        and profile_date.strftime('%m') == profile_date.strftime('%m'):
                    js = json.dumps(context, indent=4, default=json_util.default)
                    click.secho(
                        "\n [route.py]\t\tA recently downloaded JSON was found, no further requests will be sent",
                        fg="green",
                    )
                    search_stat.new_search(username)
                    return js
                else:
                    return "Username not found", 404
            else:
                return "Username not found", 404

    except IndexError:
        click.secho(
                "\n [route.py]\t\tNo JSON were found for %s, started the download process..." % username,
                fg="green",
            )
        return "Username not found", 404


'''
    For AJAX, return the comment of a given post
'''

CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/a/<shortcode>', methods=['POST'])
def post_javascript_data(shortcode):
    query = {'shortcode': shortcode}
    context = list(collection_comment.find(query))[0]
    json_comment = json.dumps(context, indent=4, default=json_util.default)    # json containing the comment list
    # make a HTTP request to parser-process and ask for sentiment analysis. r contains the response code, while r.content contians the final json
    r = requests.post('http://127.0.0.1:5002/sentiment', data = json_comment)
    sentiment_json = r.content
    print(sentiment_json)
    return sentiment_json

'''
    Return an 404 error code if the path does not match with any functions above
'''
@app.errorhandler(404)
def page_not_found(error):
    return "Requested page is not available, contact the site administrator", 404


@app.route("/")
def test():
    return "Ok",200
