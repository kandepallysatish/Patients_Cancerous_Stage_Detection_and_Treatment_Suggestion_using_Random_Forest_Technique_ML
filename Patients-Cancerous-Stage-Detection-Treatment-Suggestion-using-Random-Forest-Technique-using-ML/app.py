

from flask import Flask, render_template, url_for, request
from tensorflow.keras.models import load_model
import numpy as np
import webbrowser
import warnings
import pickle
warnings.filterwarnings("ignore")


# from flask import Flask, render_template, request
import pickle
# import numpy as np
# import webbrowser


model = pickle.load(open('RandomForest.pkl', 'rb'))
model2 = pickle.load(open('svm.pkl', 'rb'))

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':

        A1 = int(request.form['Age'])
        A2 = int(request.form['Gender'])
        A3 = int(request.form['Air Pollution'])
        A4 = int(request.form['Alcohol use'])
        A5 = int(request.form['Dust Allergy'])
        A6 = int(request.form['OccuPational Hazards'])
        A7 = int(request.form['Genetic Risk'])
        A8 = int(request.form['chronic Lung Disease'])
        A9 = int(request.form['Balanced Diet'])
        A10 = int(request.form['Obesity'])
        
        A11 = int(request.form['Smoking'])
        A12 = int(request.form['Passive Smoker'])
        A13 = int(request.form['Chest Pain'])
        A14 = int(request.form['Coughing of Blood'])
        A15 = int(request.form['Fatigue'])
        A16 = int(request.form['Weight Loss'])
        A17 = int(request.form['Shortness of Breath'])
        A18 = int(request.form['Wheezing'])
        A19 = int(request.form['Swallowing Difficulty'])
        A20 = int(request.form['Clubbing of Finger Nails'])
        
        A21 = int(request.form['Frequent Cold'])
        A22 = int(request.form['Dry Cough'])
        A23 = int(request.form['Snoring'])

        data = np.array([[A1,A2,A3,A4,A5,A6,A7,A8,A9,A10,A11,A12,A13,A14,A15,A16,A17,A18,A19,A20,A21,A22,A23]])
        my_prediction = model.predict(data)
        print(my_prediction)

        return render_template('result.html', prediction=my_prediction)
    

#webbrowser.open('http://127.0.0.1:5000/', new=2)
if __name__ == '__main__':
    app.run(port='5000')