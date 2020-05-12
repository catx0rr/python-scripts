#!/usr/bin/python3

import requests

''' 
    https://www.w3schools.com/python/module_requests.asp
    https://requests.readthedocs.io/en/master/
    https://realpython.com/python-requests/
    Methods on w3schoolsm requests.readthedocs and realpython
'''


def main():
    res = requests.get('https://www.gutenberg.org/cache/epub/1112/pg1112.txt')  # Change to your python server

    with open('exploit.py', 'wb') as download_file:  # Change this into your custom exploit file

        for chunk in res.iter_content(100000):
            download_file.write(chunk)

        download_file.close()


if __name__ == '__main__':
    main()
