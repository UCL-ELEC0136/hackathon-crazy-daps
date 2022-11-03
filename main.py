import requests

r = requests.get('https://api.github.com/orgs/Google/repos')
print(r.text)
