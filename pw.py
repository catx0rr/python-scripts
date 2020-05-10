#!/usr/bin/python3

import sys
import pyperclip


# pw.py Insecure locker program

PASSWORDS = {

    'email': 'mysupersecurepassword',
    'blog': 'helloworld123',
    'luggage': 12345

}

if len(sys.argv) < 2:
    print("Usage: pw.py [account] - copy account password")
    sys.exit()

account = sys.argv[1]  # get first argument provided on the py file

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print("Password for " + account + " copied to clipboard.")
else:
    print("There is no account named: " + account)

# use this module for automating stuff
    # email templates
    # messages that needs to be sent out repeatedly
    # Use a shell script or batch script to automate more the task
