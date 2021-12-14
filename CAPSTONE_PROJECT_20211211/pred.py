import pickle

from flask import Flask
from flask import request
from flask import jsonify


model_file = open('predict-model.bin', 'rb')
dv_file = open('dv.bin', 'rb')

model = pickle.load(model_file)
dv = pickle.load(dv_file)

def predict_result(customer, dv, model):
  X = dv.transform([customer])  ## apply the one-hot encoding feature to the customer data 
  y_pred = model.predict_proba(X)[:, 1]
  return y_pred[0]


app = Flask('pred')

@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json() 

    prediction = predict_result(customer, dv, model)
    donate = prediction >= 0.5
    result = {
        'donating_probability': float(prediction),
        'is_donating': bool(donate)
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9698)



