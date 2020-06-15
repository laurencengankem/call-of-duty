from app.start import request_to_username

from pymongo import MongoClient

client = MongoClient('3.223.148.248', 27017)
db = client['instadb']
collection_username= db['usernamedb']
collection_username.delete_many({})

try:
    while True:
        collection_username= db['usernamedb']
        usernames=list(collection_username.find({}))

        for users in usernames:
            print(users['username'])
            request_to_username(users['username'])
            collection_username.delete_one({"username":users['username']})
except:
    client = MongoClient('3.223.148.248', 27017)
    db = client['instadb']
    while True:
        collection_username= db['usernamedb']
        usernames=list(collection_username.find({}))

        for users in usernames:
            print(users['username'])
            request_to_username(users['username'])
            collection_username.delete_one({"username":users['username']})
