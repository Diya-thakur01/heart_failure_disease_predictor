from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load model and scaler
model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get values from form and convert to float
        input_features = [float(x) for x in request.form.values()]
        features_array = np.array(input_features).reshape(1, -1)

        # Scale the input features
        features_scaled = scaler.transform(features_array)

        # Predict
        prediction = model.predict(features_scaled)

        # Output message
        if prediction[0] == 1:
            result = "🚨 The patient is at risk of death."
        else:
            result = "✅ The patient is not at risk of death."

        return render_template('index.html', prediction_text=result)

    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
