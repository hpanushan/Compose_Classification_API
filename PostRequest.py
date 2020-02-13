import requests
import json

def postRequest(APIEndpoint,JSONData):
    response = requests.post(url=APIEndpoint, json=JSONData)

    responseText = response.json()

    return responseText

# Attributes
APIEndpoint = 'http://127.0.0.1:5000/'
data = {'user_input':'pack 3','options':['Package 1', 'Package 2', 'Package 3']}
json_data = json.dumps(data)

res = postRequest(APIEndpoint,json_data)

print(res)


