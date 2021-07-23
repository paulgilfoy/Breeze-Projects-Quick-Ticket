import time, requests

mylocaltime = time.strftime('%Y-%m-%d', time.localtime())


print('Hello')

print('Task Name?')
print('Department : System : Problem')
print('ex. CS : Acumatica : User Permissions issue')
breezename = input()

print('Description?')
breezedescription = input()

#API token removed for security. 
url = "http://api.breeze.pm/projects/124084/cards.json?api_token="

payload ={"name": breezename,
    "description": breezedescription,
    "startdate": mylocaltime,
    "planned_time": 120,
    "color": "c25bg",
    "stage_id": 576497,
    "swimlane_id": '',
    "invitees": ["paulg@bungalow5.com"],
    "user": {
        "id": 56539,
        "email": "paulg@bungalow5.com",
        "name": "Paul Gilfoy"}}
headers = {
  'Content-Type': 'application/json'
}

response = requests.post(url, json=payload)

print(response.text.encode('utf8'))

