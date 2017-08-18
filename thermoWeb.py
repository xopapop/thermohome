from flask import Flask, render_template
from weather import get_weather
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/slider-test')
def test_slider():
    return render_template("slider_test.html")
@app.route('/weather')
def display_weather():
    current_weather = get_weather()
    return render_template("current_weather.html",weather=current_weather)

if __name__ == '__main__':
    app.run()
