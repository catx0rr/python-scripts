#!/usr/bin/python3

'''
    tbrowse.py - Launches web browser by providing URL in the command line.
'''

import webbrowser
import re
import sys
import time


url_gex = re.compile(r'((http|www\.|https)?(://)?[a-zA-Z0-9.-_]+\.[a-zA-Z]{1,3})')

err = '[-] Usage: tbrowse.py [URL]'


def browse(url):
    try:

        if url_gex.search(url).group():
            print('[+] Opening %s' % (url))
            time.sleep(1.5)
            webbrowser.open(url)

    except AttributeError:
        print(err, '\n[-] ERROR: Invalid URL.')


if __name__ == '__main__':

    if len(sys.argv) < 2 or len(sys.argv) > 2:
        print(err, '\n[-] ERROR: Insufficient arguments. Terminating.')
        sys.exit(1)

    else:
        browse(sys.argv[1])
        sys.exit(0)
