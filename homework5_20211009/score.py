import pickle

from flask import Flask
from flask import request
from flask import jsonify

#import requests

##url = "YOUR_URL"
##customer = {"contract": "two_year", "tenure": 1, "monthlycharges": 10}
##requests.post(url, json=customer).json()

model_file = open('model2.bin', 'rb')
dv_file = open('dv.bin', 'rb')

model = pickle.load(model_file)
dv = pickle.load(dv_file)

def predict_single(customer, dv, model):
  X = dv.transform([customer])  ## apply the one-hot encoding feature to the customer data 
  y_pred = model.predict_proba(X)[:, 1]
  return y_pred[0]


app = Flask('score')

@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json() 

    prediction = predict_single(customer, dv, model)
    churn = prediction >= 0.5
    result = {
        'churn_probability': float(prediction),
        'churn': bool(churn)
    }

    return jsonify(result)

##if __name__ == "__main__":
##    app.run(debug=True, host='0.0.0.0', port=9698)


