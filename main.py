import requests
import pymongo

server = pymongo.MongoClient("mongodb+srv://student:assignment@cluster0.iqqk4u7.mongodb.net/?retryWrites=true&w=majority")
page = 1
while True:
    r_google = requests.get("https://api.github.com/orgs/google/repos?per_page=100&page={}".format(page))
    repo = r_google.json()
    if len(repo) == 0:
        break

    database = server["hackathon"]
    collection = database["repo"]
    collection.insert_many(repo)

    page += 1



