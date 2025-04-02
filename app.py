from flask import Flask, request, render_template
import pandas as pd

from src.pipeline.predict_pipeline import CustomData, PredictPipeline

from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictData', methods=['POST','GET'])
def predict_datapoints():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        data = CustomData(
            km_driven=float(request.form.get('km_driven')),
            vehicle_age=int(request.form.get('vehicle_age')),
            seller_type=request.form.get('seller_type'),
            fuel_type=request.form.get('fuel_type'),
            transmission_type=request.form.get('transmission_type'),
            mileage=float(request.form.get('mileage')),
            engine=float(request.form.get('engine')),
            max_power=float(request.form.get('max_power')),
            seats=int(request.form.get('seats'))
        )

        pred_data = data.get_data_as_dataframe()

        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_data)

        return render_template('form.html', results=int(results[0]))
    
if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)