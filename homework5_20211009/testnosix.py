import requests

customer = {'contract': 'two_year', 'tenure': 12, 'monthlycharges': 10}
url = "http://localhost:9698/predict"
response = requests.post(url, json=customer).json()
result = response
print(result)