from flask import Flask, request

app = Flask(__name__)

@app.route('/temperature-alert', methods=["POST"])
def temperature_alert():
    data = request.get_json()
    print(data)
    return ''

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0')