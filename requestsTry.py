import requests
import json
auth = "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"
headers = {'Authorization': 'token '+ auth, 'user': 'bxa170'}

login = requests.get("https://api.github.sherwin.com/user", headers=headers)
print(json.dumps(login.json(), indent=4, sort_keys=True))
print(login.json()['name'])
# using asterisk
# num = [1,12,3,4,5,6]

# print(sum(num))
# print(num)
