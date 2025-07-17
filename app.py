from flask import Flask, render_template,request, Response, send_from_directory,jsonify
import pandas as pd
import os
import uuid


app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/')



@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')