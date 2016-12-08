import requests, json

github_url = "https://api.github.com/user/repos"
data = json.dumps({'name':'test_repo', 'description':'some test repo'})
r = requests.post(github_url, data, auth=('richardegenas', ''))

print(r.json)