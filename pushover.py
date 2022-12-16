import requests


def send_alert(api_key, group_key, message):
    return requests.post(
        'https://api.pushover.net/1/messages.json',
        
        data = {
            'token': api_key,
            'user': group_key,
            'message': message
        }
    )
