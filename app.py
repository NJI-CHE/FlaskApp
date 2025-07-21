from flask import Flask, render_template,request, Response, send_from_directory,jsonify, session, make_response, Request, flash
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
        if 'name' not in session:
            session['name'] = 'Nji'
        if 'other' not in session:
            session['other'] = 'Njuila'
        return render_template('index.html', message= 'Session data set')
    else:
        return render_template('index.html', message='No Sessions found')
@app.route('/get_data')
def get_data():
    name = session['name']
    other = session['other']
    return render_template('index.html', message = f'Name: {name}, Other: {other}')

@app.route('/clear_session')
def clear_session():
    session.clear()
    return render_template('index.html', message='The session was cleared')

@app.route('/set_cookie')
def set_cookie():
    response = make_response(render_template('index.html', message = 'Cookie Set!'))
    response.set_cookie(key='cookie_name', value= 'cookie_value')
    return response

@app.route('/get_cookie')
def get_cookie():
    cookie_value = request.cookies['cookie_name']
    return render_template('index.html', message = f'cookie Value: {cookie_value}')

@app.route('/remove_cookie')
def remove_cookie():
    response = make_response(render_template('index.html', message = 'Cookie removed!'))
    response.set_cookie(key='cookie_name', expires=0)
    return response

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'nji' and password == 'code':
            flash('successful Login!')
            return render_template('index.html', message = '')
        else:
            flash('Login failed!')
            return render_template('index.html', message='')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')