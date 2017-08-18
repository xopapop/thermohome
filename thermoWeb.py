from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/slider-test')
def test_slider():
    return render_template("slider_test.html")
if __name__ == '__main__':
    app.run()
