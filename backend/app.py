from flask import Flask, render_template
import time


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/time')
def get_current_time():
    return {'time': time.time()}
