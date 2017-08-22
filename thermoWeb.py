from flask import Flask, render_template, request, jsonify
import json
from weather import get_weather
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/slider-test', methods=['GET', 'POST'])
def test_slider():
    return render_template("slider_test.html")

@app.route('/slider-out', methods=['POST'])
def slider_out():
    r =json.loads(request.data.decode("utf-8"))
    print(r)
    min_temp = r['minimum']
    max_temp = r['maximum']
    return jsonify(min_temp=min_temp, max_temp=max_temp)

@app.route('/weather')
def display_weather():
    current_weather = get_weather()
    return render_template("current_weather.html", weather=current_weather)

if __name__ == '__main__':
    app.run()
