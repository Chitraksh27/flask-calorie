from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import IntegerField, DecimalField, SubmitField, SelectField
from wtforms.validators import InputRequired, NumberRange
import joblib
import pandas as pd
import gdown
import os

MODEL_URL = "https://drive.google.com/uc?id=1kWDn6j2TPNt4mwNJF0KhA7I4pynVMKYe"
MODEL_PATH = "calories_burnt.sav"

if not os.path.exists(MODEL_PATH):
    print("Downloading model from Google Drive...")
    gdown.download(MODEL_URL, MODEL_PATH, quiet = False)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'iamyourgrowth'

model = joblib.load('calories_burnt.sav')
scaler = joblib.load('scaler.pkl')
encoder = joblib.load('gender_encoder.pkl')

class CalorieForm(FlaskForm):
    gender = SelectField('Gender', choices = [('male', 'Male'), ('female', 'Female')], validators = [InputRequired()])
    age = IntegerField('Age', validators = [InputRequired(), NumberRange(min = 20, max = 80, message = "Enter valid age between 20 and 80 years")])
    height = IntegerField('Height (in cm)', validators = [InputRequired()])
    weight = IntegerField('Weight (in kg)', validators = [InputRequired()])
    duration = IntegerField('Duration (in minutes)', validators = [InputRequired()])
    heart_rate = IntegerField('Heart Rate (in beats per minute)', validators = [InputRequired()])
    body_temp = DecimalField('Body Temperature (in °C)', validators = [InputRequired()])
    submit = SubmitField('Predict')


@app.route('/')
@app.route('/predict', methods = ['GET', 'POST'])
def predict():
    form = CalorieForm()
    prediction = None
    pred_tips1 = [
        "Aim for ~500 ml of water plus a light electrolyte drink if execessive sweating occurs.",
        "5-10 mins of gentle stretching or a slow walk to help clear metabolic byproducts and reduce soreness.",
        "If you did something high-intensity (HIIT, heavy circuit), give yourself a day-off or low-intensity active recovery tomorrow."
    ]
    pred_tips2 = [
        "Burning 100-200 kcal daily is fantastic for building a habit - keep showing up!",
        "Spend 5 minutes on dynamic stretches (leg swings, arm circles) to improve flexibility and reduce injury risk.",
        "If your goal is to burn more calories, add 5 minutes or increase intensity by choosing slightly faster pace or adding gentle inclines."
    ]
    pred_tips3 = [
        "Add 10-15 extra minutes of moderate activity - brisk walking, light cycling, or body-weight moves like squats, lunges and push-ups.",
        "Make sure your movements engage the big muscle groups fully: full range-of-motion squats, proper lunge form, core-tight planks.",
        "Introduce short intervals of higher intensity - 30 seconds of faster pace or incline every 2-3 minutes to boost calorie burn."
    ]
    if form.validate_on_submit():
        gender_num = encoder.transform([form.gender.data])[0]
        feature_df = pd.DataFrame({
            'Gender': [gender_num],
            'Age': [form.age.data],
            'Height': [form.height.data],
            'Weight': [form.weight.data],
            'Duration': [form.duration.data],
            'Heart_Rate': [form.heart_rate.data],
            'Body_Temp': [float(form.body_temp.data)]
        })
        feature_scale = scaler.transform(feature_df)
        prediction = round(model.predict(feature_scale)[0], 2)
        return render_template('form.html', form = form, prediction = prediction, pred_tips1 = pred_tips1, pred_tips2 = pred_tips2, pred_tips3 = pred_tips3)
    return render_template('form.html', form = form, prediction = prediction, pred_tips1 = pred_tips1, pred_tips2 = pred_tips2, pred_tips3 = pred_tips3)

if __name__ == "__main__":
    app.run(debug = True)