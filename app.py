from flask import Flask, render_template,request, Response
import pandas as pd

app = Flask(__name__, template_folder='templates')



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == 'nji' and password == 'pass':
            return 'success'
        else:
            return 'Failed login'
        
@app.route('/file_upload', methods=['POST'])
def file_upload():
    file = request.files['file']

    if file.content_type == 'text/plain':
        return file.read().decode()
    elif file.content_type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' or file.content_type == 'application/vnd.ms-excel':
        df = pd.read_excel(file)
        return df.to_html()


@app.route('/convert_csv', methods=['POST'])
def convert_csv():
    file = request.files['file']

    df = pd.read_csv(file)

    response  = Response(
        df.to_csv(index=False),
        mimetype='text/csv',

        headers={
            'Content-Disposition': 'attachment; filename=results.csv'
        }
    )

    return response


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')