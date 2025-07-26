# 🔥 Calorie Burnt Predictor

A lightweight, web-based tool built using **Flask** and **Machine Learning** that estimates the number of calories you've burned during a workout - based on your physical stats and workout intensity.

## 🚀 What It Does

You enter your:
- Gender
- Age
- Height (in cm) and Weight (in kg)
- Duration of exercise (in minutes)
- Heart Rate
- Body Temperature (in °C)  
... and it predicts how many **calories** you've likely burned 🔥  
It also gives **fitness suggestions** tailored to your result range (light, moderate, intense).

---

## 🧠 How it Works
- Trained on a real-world dataset from [Kaggle](https://www.kaggle.com/datasets/ruchikakumbhar/calories-burnt-prediction)
- Model: `RandomForestRegressor` from `scikit-learn`
- Optimized using `GridSearchCV` for best hyperparameters
- Inputs are preprocessed (scaled + encoded) before prediction
- Web app built with:
    - `Flask`
    - `WTForms`
    - `Jinja2`
    - `joblib` for model and scaler serialization

---

## 💻 Tech Stack 

| Component      | Tech Used                   |
|----------------|-----------------------------|
| Web Framework  | Flask                       |
| ML Model       | Random Forest Regressor     |
| Frontend Rendering | HTML5, CSS3, Jinja2 Templates | 
| Forms & Validation | Flask-WTForms           |
| Dataset         | Kaggle (Calories Burnt Prediction)  |
| Model Optimization | GridSearchCV            |

## ⚙️ Installation Instructions
```bash
# 1. Clone the repo
git clone https://github.com/web-calorie-predictor.git
cd web-calorie-predictor

# 2. Create virtual environment
python -m venv venv
venv\Scripts\activate # On Windows
# On Linux source venv/bin/activate

# 3. Install requirements
pip install -r requirements.txt

# 4. Run the app
python app.py
```

## 📌 To-Do / Future Ideas
- Add dark mode toggle
- Add deployment on Render/Heroku

## 👨‍💻 Made By 
**Chitraksh Sharma**  
[LinkedIn](https://www.linkedin.com/in/chitraksh-sharma-2a3564329/) | [Github](https://github.com/Chitraksh27)

## ⚠️ Disclaimer
This tool is **not a medical device** and should be used for **informational purposes** only. The prediction is based on statistical patterns from fitness data and may not perfectly reflect personal metabolic conditions.

## Note
This app uses a **Random Forest Regressor** model to estimate calories burned based on user input (age, gender, weight, etc).  

To avoid uploading large model files to Github, the model is hosted on **Google Drive** and will be **automatically downloaded** when you run the app for the first time.  

No manual setup needed - just run the app and let it fetch what it needs  

**Files Downloaded at runtime**: `calories_burnt.sav` (Trained RandomForestRegressor model)  

**Make sure you are connected to the Internet during the first run so the files can be downloaded successfully**