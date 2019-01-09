import json
import requests

ApiKey = 'lPpKLU2BhzWU3eB2iWHeZ0XG5fO241JP'
base_url = 'http://forex.1forge.com/1.0.3/'

def main():
    response = requests.get(base_url + 'symbols' + '?api_key=' + ApiKey)
    list_of_symbols = response.json()
    print(list_of_symbols)
    requests.get('http://forex.1forge.com/1.0.3/')
    print('hello')


if __name__ == '__main__':
	main()
