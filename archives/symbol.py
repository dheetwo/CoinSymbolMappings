import requests

api_key = 'freekey'
url_header = 'https://api.ethplorer.io/'

def get_token_data(contract_address):
    request = 'getTokenInfo'
    url = f"{url_header}{request}/{contract_address}?apiKey={api_key}"
    response = requests.get(url)
    data = response.json()
    return data

def extract_symbol(data, contract_address):
    return data.get('symbol')