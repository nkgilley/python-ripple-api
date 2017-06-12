"""Python API for using ripple.com."""
import requests

BASE_URL = 'https://data.ripple.com/v2/accounts/'

def get_balance(address):
    req_url = BASE_URL + address + '/balances'
    response = requests.get(req_url).json()
    if response.get('result'):
        if response.get('result') == 'success':
            return float(response['balances'][0]['value'])
