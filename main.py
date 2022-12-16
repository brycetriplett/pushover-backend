from flask import Flask, request
app = Flask(__name__)

from config import pushover_args
from pushover import send_alert


@app.route('/alert', methods=["POST"])
def temperature_alert():
    data = request.get_json()
    
    result = send_alert(
        **pushover_args,
        message=data['_message']
    )

    return str(result.status_code)


if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0')