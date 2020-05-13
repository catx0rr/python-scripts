#!/usr/bin/python3

'''
    googl.py - perform multiple (5) max searches on the terminal and open a browser.

'''

import requests
import sys
import webbrowser
import bs4
import time

err = 'Usage: googl.py [search] [search] [search] [search] [search]'


def googl(*args):
    print('[>] Googling...')
    time.sleep(1)

    with requests.get("https://www.google.com/search?q=" + ' '.join(*args)) as req:
        req.raise_for_status()

    # Retrieve top search result links.
    soup = bs4.BeautifulSoup(req.text, features="html.parser")

    # Open a browser tab for each result.
    link_elems = soup.select('.r a')

    num_open = min(5, len(link_elems))
    for i in range(num_open):
        webbrowser.open('https://google.com' + link_elems[i].get('href'))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(err, '\n[-] Insufficient Arguments.')
        sys.exit(1)

    else:
        googl(sys.argv[1:])
        print('[-] Done.')
        sys.exit(0)
