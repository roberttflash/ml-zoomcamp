import pickle

model_file = open('model1.bin', 'rb')
dv_file = open('dv.bin', 'rb')

model = pickle.load(model_file)
dv = pickle.load(dv_file)

customer = {"contract": "two_year", "tenure": 12, "monthlycharges": 19.7}

X = dv.transform([customer])
y_pred = model.predict_proba(X)[0,1]
churn = y_pred >= 0.5

print('churn_probability: ', y_pred)
print('churn: ', churn)