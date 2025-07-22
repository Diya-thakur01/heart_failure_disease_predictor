Heart Failure Prediction using Flask
This project is a simple web application built with Flask that predicts whether a person is likely to suffer from heart failure based on medical parameters using a trained machine learning model.

 Features
Predicts heart failure based on user input

Flask-based web app with HTML & CSS frontend

Trained ML model (model.pkl)

Scaler for input normalization (scaler.pkl)

 Technologies Used
Python

Flask

HTML/CSS

Machine Learning (Logistic Regression / Random Forest)

Scikit-learn, NumPy, Pandas

 Project Structure
php
Copy
Edit
├── app.py                 # Main Flask app
├── model_training.ipynb   # Jupyter notebook for model training
├── model.pkl              # Saved ML model
├── scaler.pkl             # Saved scaler object
├── templates/             # HTML files
│   └── index.html
├── static/                # CSS files
│   └── style.css
 How to Run Locally
bash
Copy
Edit
git clone (https://github.com/Diya-thakur01/heart_failure_disease_predictor)
 
cd heart-failure-predictor
pip install -r requirements.txt
python app.py
Go to http://127.0.0.1:5000/ in your browser.

 Example Inputs
Age

Chest pain type

Cholesterol level

Maximum heart rate

... and other features used in training

 Screenshots
<img width="1888" height="1024" alt="image" src="https://github.com/user-attachments/assets/4587c0ba-a5f0-4102-aae0-2bb863aca7d4" />


 Author
Diya Thakur
B.Tech CSE (AI/ML), SVSU

 License
This project is licensed under the MIT License.
