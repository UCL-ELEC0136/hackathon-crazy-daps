import requests
import pymongo

google_data = requests.get('https://api.github.com/orgs/Google/repos')
print(google_data.text)

client = pymongo.MongoClient("mongodb+srv://student:assignment@cluster0.iqqk4u7.mongodb.net/?retryWrites=true&w=majority")
db= client.admin
db = client.daps_hackathon

# Upload to MangoDB
collection = db.daps_hackathon
upload1 = collection.insert_many(google_data)


