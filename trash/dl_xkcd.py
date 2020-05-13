#!/usr/bin/python3

# dl_xkcd.py - Download every single XKCD comic.

import requests
import os
import bs4
import time

url = 'http://xkcd.com'             # starting url
os.makedirs('xkcd', exist_ok=True)  # store comics in ./xkcd

while not url.endswith('#'):

    # Download the page
    print('[>] Downloading page %s...' % (url))
    time.sleep(1)
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, features='html.parser')

    # Find the URL of the comic image.
    comic_elem = soup.select('#comic img')
    if comic_elem == []:
        print('[-] Could not find comic image.')

    else:
        comic_url = comic_elem[0].get('src')

        # Download the image
        print('[>] Downloading image %s...' % (comic_url))
        time.sleep(1.75)
        res = requests.get(comic_url)
        res.raise_for_status()

        # Save the image to ./xkcd
        with open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb') as image_file:
            for chunk in res.iter_content(100000):
                image_file.write(chunk)
            image_file.close()

        # Get the prev button's url
        prev_link = soup.select('a[rel="prev"]')[0]
        url = 'http://xkcd.com' + prev_link.get('href')

print('[+] Done.')
