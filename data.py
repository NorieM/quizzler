import requests

URI = 'https://opentdb.com/api.php'

parameters = {'amount': 10,
              'difficulty': 'easy',
              'type': 'boolean',
              'token': 'd5b32d449f63c4353652fb8e59590c0624f6d7a50693dc16172c5e59cd73c62a'}

response = requests.get(URI, parameters)
response.raise_for_status()
data = response.json()
print(data)
question_data = data['results']

