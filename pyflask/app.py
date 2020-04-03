from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template(
        'index.html',
        title = 'Flask Template Test',
        home_str = 'Hello Flask!',
        home_list = [1, 2, 3, 4, 5])

@app.route('/info')
def info():
    return render_template('info.html')
