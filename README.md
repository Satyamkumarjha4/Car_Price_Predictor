# Car Price Prediction

## Overview
This project is designed to explore various machine learning models and hyperparameter tuning techniques. It predicts the price of second-hand cars based on their specifications using a dataset of approximately 15,000 records. The project involves data preprocessing, model training, and deployment via a Flask-based web application.

## Features
- Data preprocessing, feature engineering, and transformation
- Model training and evaluation (using multiple regression models)
- Web-based user interface for car price prediction
- Deployment on Render for easy access

## Tech Stack
- **Programming Language**: Python
- **Libraries Used**: Pandas, NumPy, Scikit-Learn, Pickle, CatBoost, Flask
- **Web Framework**: Flask
- **Frontend**: HTML, CSS (Basic Form and Display Page)
- **Deployment**: Render ([Live Link](https://car-price-predictor-4aiw.onrender.com/))

## Machine Learning Models Used
Several regression models were trained, and the best model was selected based on performance:
- **Linear Regression**
- **Random Forest**
- **Decision Tree**
- **AdaBoost**
- **XGBoost**
- **CatBoost** (Best performing model with 91% accuracy)

## Project Structure
```
CAR_PRICE/
│── artifacts/               # Stores model and preprocessor pickle files
│   │── model.pkl
│   │── preprocessor.pkl
│── notebook/                # Jupyter Notebooks for EDA and Model Training
│   │── EDA_CAR_PRICE.ipynb
│   │── 2. MODEL TRAINING.ipynb
│── src/                     # Source code
│   │── components/           # Data processing components
│   │   │── data_ingestion.py
│   │   │── data_transformation.py
│   │   │── model_trainer.py
│   │── pipeline/             # Training and prediction pipelines
│   │   │── train_pipeline.py
│   │   │── predict_pipeline.py
│   │── utils.py              # Utility functions
│   │── logger.py             # Logging module
│── templates/                # HTML Templates
│   │── index.html
│   │── form.html
│── app.py                    # Flask Web Application
│── requirements.txt          # Dependencies
│── setup.py                  # Package setup
│── README.md                 # Project Documentation
```

## Data Flow (Pipeline)
1. **Data Ingestion (`data_ingestion.py`)**: Reads and splits data into training and test sets.
2. **Data Transformation (`data_transformation.py`)**: Feature engineering, missing value imputation, and encoding.
3. **Model Training (`model_trainer.py`)**: Trains multiple models and selects the best based on R² score.
4. **Prediction Pipeline (`predict_pipeline.py`)**: Loads the trained model and preprocessor to make predictions.
5. **Web Application (`app.py`)**: Provides a user interface to input car details and get price predictions.

## Installation & Setup
To run this project locally:

1. **Clone the repository**
   ```sh
   git clone <repo-link>
   cd CAR_PRICE
   ```
2. **Create a virtual environment**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate     # On Windows
   ```
3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```
4. **Run the application**
   ```sh
   python app.py
   ```
5. Open your browser and go to `http://127.0.0.1:8080/`

## Usage
- Navigate to the **index page** (`index.html`) for an introduction.
- Enter car details in the **form page** (`form.html`).
- Click submit to get the predicted price.

## Deployment
The project is deployed on Render:
[https://car-price-predictor-4aiw.onrender.com/](https://car-price-predictor-4aiw.onrender.com/)

## Future Enhancements
- Improve UI/UX of the web interface
- Deploy on AWS/GCP for scalability
- Add more advanced ML models for better accuracy
- Enable API-based interaction for external applications

## Contact
For any queries, feel free to reach out:
- **Developer**: Satyam Kumar Jha
- **Email**: satyamjha4@gmail.com


