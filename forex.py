import json
import requests

ApiKey = 'lPpKLU2BhzWU3eB2iWHeZ0XG5fO241JP'
base_url = 'http://forex.1forge.com/1.0.3/'

def get_currency_quotes():
    quote_url = 'http://forex.1forge.com/1.0.3/quotes?pairs='
    list_of_symbols = requests.get(base_url + 'symbols?' + 'api_key=' + ApiKey).json()

    for symbol in list_of_symbols:
        quote_url = quote_url + symbol + ','
    quote_url = quote_url[:-1] + '&api_key=' + ApiKey
    currency_quotes = requests.get(quote_url).json()
    return currency_quotes

def main():
    quote_url = 'http://forex.1forge.com/1.0.3/quotes?pairs='
    response = requests.get(base_url + 'symbols?' + 'api_key=' + ApiKey)
    list_of_symbols = response.json()

    for symbol in list_of_symbols:
        quote_url = quote_url + symbol + ','
    quote_url = quote_url[:-1] + '&api_key=' + ApiKey
    print(quote_url)
    currency_quotes = requests.get(quote_url).json()

    for currency in currency_quotes:
        


if __name__ == '__main__':
	main()
