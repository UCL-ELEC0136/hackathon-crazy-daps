import requests
import pymongo


client = pymongo.MongoClient("mongodb+srv://student:assignment@cluster0.iqqk4u7.mongodb.net/?retryWrites=true&w=majority")
db = client.daps_hackathon

# # Upload to MangoDB
collection = db.daps_hackathon


repo_per_page = []
page = 1

while True:
    url = "https://api.github.com/orgs/Google/repos?per_page=100&page={}".format(page)
    response = requests.get(url, auth=('Deng-1-Pan', "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"))
    
    repos = response.json()
    if len(repos) == 0:
        break
    
    # repo_per_page.append(repos)
    
    upload1 = collection.insert_many(repos)
    
    page += 1
# client = pymongo.MongoClient("mongodb+srv://student:assignment@cluster0.iqqk4u7.mongodb.net/?retryWrites=true&w=majority")
# db= client.admin


