import requests
import json

url = 'http://127.0.0.1:5000/node-recv'

with open('sample-gpt.json', 'r') as sample:
    data = json.load(sample)

sample_packet = data

json_data = json.dumps(sample_packet)

headers = {'Content-Type': 'application/json'}

# Send the POST request
response = requests.post(url, data=json_data, headers=headers)

# Print the response from the server
print("Response from server:")
print(response.text)
