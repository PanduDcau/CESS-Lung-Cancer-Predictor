from flask import Flask, request, url_for, redirect, render_template
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

# model = pickle.load(open('Lung_Cancer.pkl', 'rb'))

filename = 'Lung_Cancer.pkl'
with open(filename, 'rb') as f:
    model = pickle.load(f)


@app.route('/')
def hello_world():
    return render_template("lung_cancer.html")


# Parameters used for Prediction
# ['GENDER', 'AGE', 'SMOKING', 'YELLOW_FINGERS', 'ANXIETY',
#        'PEER_PRESSURE', 'CHRONIC DISEASE', 'FATIGUE ', 'ALLERGY ', 'WHEEZING',
#        'ALCOHOL CONSUMING', 'COUGHING', 'SHORTNESS OF BREATH',
#        'SWALLOWING DIFFICULTY', 'CHEST PAIN', 'LUNG_CANCER']

FEATURE_NAMES = [
    'GENDER', 'AGE', 'SMOKING', 'YELLOW_FINGERS', 'Anxiety',
    'PEER_PRESSURE', 'CHRONIC DISEASE', 'FATIGUE', 'ALLERGY', 'WHEEZING',
    'ALCOHOL CONSUMING', 'COUGHING', 'SHORTNESS OF BREATH',
    'SWALLOWING DIFFICULTY', 'CHEST PAIN'
]


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        missing = [name for name in FEATURE_NAMES if not request.form.get(name, '').strip()]
        if missing:
            return render_template(
                'lung_cancer.html',
                pred='Please fill in all fields (missing: {}).'.format(', '.join(missing))
            )
        try:
            int_features = [int(request.form[name]) for name in FEATURE_NAMES]
        except ValueError:
            return render_template(
                'lung_cancer.html',
                pred='Invalid input: please enter valid numbers for all fields.'
            )
        final = np.reshape(int_features, (1, -1))
        print(int_features, flush=True)  # Checking Inputs Successfully Added
        prediction = model.predict(final)
        print(prediction, flush=True)  # Checking the Prediction Value
        output = int(prediction[0])
        if output == 0:
            return render_template('lung_cancer.html', pred='Person Has Lung Cancer ({})'.format(output))
        else:
            return render_template('lung_cancer.html', pred='Person Does Not Have Lung Cancer ({})'.format(output))
    else:
        return render_template('lung_cancer.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True, port=8000)
