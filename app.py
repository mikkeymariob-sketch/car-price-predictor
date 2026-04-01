from flask import Flask, request, jsonify, render_template
import pickle, json, numpy as np

app = Flask(__name__)

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)
with open('encoders.pkl', 'rb') as f:
    encoders = pickle.load(f)
with open('dropdown_data.json', 'r') as f:
    dropdown_data = json.load(f)

@app.route('/')
def index():
    return render_template('index.html', dropdown_data=dropdown_data)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        cat_cols = ['Manufacturer','Category','Leather interior','Fuel type','Gear box type','Drive wheels','Wheel']
        for col in cat_cols:
            val = data[col]
            if val not in encoders[col].classes_:
                return jsonify({'error': f'Unknown value for {col}: {val}'}), 400
            data[col] = int(encoders[col].transform([val])[0])

        features = [
            float(data['Prod. year']),
            float(data['Levy']),
            float(data['Engine volume']),
            float(data['Mileage']),
            float(data['Cylinders']),
            float(data['Airbags']),
            float(data['Manufacturer']),
            float(data['Category']),
            float(data['Leather interior']),
            float(data['Fuel type']),
            float(data['Gear box type']),
            float(data['Drive wheels']),
            float(data['Wheel']),
        ]
        pred = model.predict([features])[0]
        return jsonify({'price': round(float(pred), 2)})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
