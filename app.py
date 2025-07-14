from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')



@app.route('/')
def index():
    myValues = "Njiche.dev"
    myList = [1, 2, 3, 4, 5]
    return render_template('index.html', myList=myList)

@app.route('/other')
def other():
    myValues = "Njiche.dev"
    myList = [1, 2, 3, 4, 5]
    someText = 'Hello World'
    return render_template('other.html', someText=someText)

@app.template_filter('reverseString')
def reverseString(s):
    return s[::-1]

@app.template_filter('repeat')
def repeat(s, times=5):
    return s * times

@app.template_filter('alternateCase')
def alternateCase(s):
    return ''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(s)])

        


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')