from pymongo import MongoClient

client = MongoClient('3.223.148.248', 27017)
db = client['instadb']
collection_username= db['profiledb']
print(len(list(collection_username.find({}))))
client.close()
