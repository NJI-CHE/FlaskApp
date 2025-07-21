from flask import Flask, render_template,request, Response, send_from_directory,jsonify, session, make_response
import pandas as pd
import os
import uuid


app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/')
app.secret_key = 'testFlask'



@app.route('/')
def index():
    return render_template('index.html', message='Index')

@app.route('/set_data')
def set_data():
    if 'name' in session.keys() and 'other' in session.keys():
        session['name'] = 'Nji'
        session['other'] = 'Njuila'
        return render_template('index.html', message= 'Session data set')
    else:
        return render_template('index.html', message='No Sessions found')
@app.route('/get_data')
def get_data():
    name = session['name']
    other = session['other']
    return render_template('index.html', message = f'Name: {name}, Other: {other}')

@app.route('/cleare_session')
def clear_session():
    session.clear()
    return render_template('index.html', message='The session was cleared')

@app.route('set-cookie')
def set_cookie():
    response = make_response(render_template('index.html', message = 'Cookie Set!'))
    response.set_cookie(key:'cookie_name', value: 'cookie_value')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')