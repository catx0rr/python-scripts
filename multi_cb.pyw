#!/usr/bin/python3

'''
multi_cb.pyw - Saves and loads pieces of text to clipboard

Usage:  py.exe multi_cb.pyw save <keyword> - Saves clipboard to keyword
        py.exe multi_cb.pyw <keyword> Loads keyword to clipboard.
        py.exe multi_cb.pyw list - Loads all keywords to clipboard.

'''

import shelve
import pyperclip
import sys

with shelve.open('mcb_db') as database:
    try:
        if len(sys.argv) == 3 and sys.argv[1].lower == 'save':
            database[sys.argv[2]] = pyperclip.paste()

        elif len(sys.argv) == 2:
            # List keywords and load content
            if sys.argv[1].lower() == 'list':
                pyperclip.copy(str(list(database.keys())))

            elif sys.argv[1] in database:
                pyperclip.copy(database[sys.argv[1]])
                print(database[sys.argv[1]])

    except IndexError:
        print('[-] No argument parsed.')

database.close()
