import requests

customer = {
'checking_status': "'<0'",
 'duration': 36,
 'credit_history': "'critical/other existing credit'",
 'purpose': 'education',
 'credit_amount': 8065,
 'savings_status': "'<100'",
 'employment': "'1<=X<4'",
 'installment_commitment': 3,
 'personal_status': "'female div/dep/mar'",
 'other_parties': 'none',
 'residence_since': 2,
 'property_magnitude': "'no known property'",
 'age': 25,
 'other_payment_plans': 'none',
 'housing': 'own',
 'existing_credits': 2,
 'job': "'high qualif/self emp/mgmt'",
 'num_dependents': 1,
 'own_telephone': 'yes',
 'foreign_worker': 'yes'
}


#url = "http://localhost:9696/predict"
url = "https://zoomcamp-midterm.herokuapp.com/predict"
response = requests.post(url, json=customer).json()
result = response
print(result)