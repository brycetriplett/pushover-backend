from crypt import methods
from flask import Flask, request
app = Flask(__name__)

@app.route('/temperature-alert', methods=["POST"])
def hello_world():
    # for x in request:
    #     print(x)
    print(request.data)
    return ''

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0')