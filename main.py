from flask import Flask, request
app = Flask(__name__)

@app.route('/temperature-alert')
def hello_world():
    print(request.form)
    return ''

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0')