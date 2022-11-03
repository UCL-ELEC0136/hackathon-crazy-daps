import requests
import pymongo

r = requests.get('https://api.github.com/orgs/Google/repos')
print(r.text)

client = pymongo.MongoClient("mongodb+srv://student:assignment@cluster0.iqqk4u7.mongodb.net/?retryWrites=true&w=majority")
