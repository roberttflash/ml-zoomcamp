import requests

url = 'http://localhost:8080/2015-03-31/functions/function/invocations'
#url = 'https://98rbnzdyec.execute-api.ap-southeast-1.amazonaws.com/test/predict'

data = {'url': 'https://upload.wikimedia.org/wikipedia/commons/1/18/Vombatus_ursinus_-Maria_Island_National_Park.jpg'}

result = requests.post(url, json=data).json()
print(result)
