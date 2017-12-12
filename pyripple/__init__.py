"""Python API for using ripple.com."""
import requests

BASE_URL = 'https://data.ripple.com/v2/accounts/'

def get_balance(address):
    req_url = BASE_URL + address + '/balances'
    response = requests.get(req_url)
    if response.status_code == 200 and response.json().get('result'):
        if response.json().get('result') == 'success':
            return float(response.json()['balances'][0]['value'])
