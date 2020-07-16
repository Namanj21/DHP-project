from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin','*')

    return response

@app.route('/predict_home_price', methods=['POST'])

def predict_home_price():
    area = float(request.form['area'])
    location = request.form['location']
    bhk = int(request.form['bhk'])

    response=jsonify({
          'estimated_price': util.get_estimated_price(location,area,bhk)

    })

    response.headers.add('Access-Control-Allow-Origin','*')

    return response

if __name__ == "__main__":
    print("Starting Python flask server for delhi Price Prediction...")
    util.load_saved_artifacts()
    app.run()
