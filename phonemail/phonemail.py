#!/usr/bin/python3

# phone_email.py regex for emails and phone numbers

import pyperclip
import re
import sys


phone_regex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?           # Philippine area code
    (\s|-|\.)?                   # separator
    (\d{3})                      # first 3 digits
    (\s|-|\.)                    # separator
    (\d{4})                      # last 4 digits
    (\*(ext|x|ext.)\*(\d{2,5}))? # optional extension number
    )''', re.VERBOSE)


email_regex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+            # username
    @                            # @ symbol
    [a-zA-Z0-9.-]+               # domain name
    (\.[a-zA-Z]{1,4})            # top level domain
    )''', re.VERBOSE)


# Start Prompt
print(''' >>> phone-email-regex <<<
Usage: Copy text and find the matching keywords.
    ''')

if not pyperclip.paste():
    print('''[-] Copy first texts and will find the email and phone numbers matching.
    >>> Examples <<<
    Hello user, my email is email@sample.com and my phone number is 632-442-821
    [+] Match found:

    email@sample.com 
    632-442-821
        ''')
    sys.exit(1)


while True:
    # Find matches in clipboard text
    text = str(pyperclip.paste())

    # print(phone_regex.findall(text))

    matches = []                                                    # empty container for regex matching
    for groups in phone_regex.findall(text):
        phone_num = '-'.join([groups[1], groups[3], groups[5]])     # join from regex list, 1: area_code 3: first 3 digits 5: last four digits

        if groups[8] != '':                                         # match for extension if not empty
            phone_num += ' ext: ' + groups[8]                       # added ext: before the number

        matches.append(phone_num)

    for groups in email_regex.findall(text):
        matches.append(groups[0])                                   # find all the email match

    # Copy results to clipboard
    if len(matches) > 0:
        pyperclip.copy('\n'.join(matches))
        print('[+] Match Found.\n[+] Copied to clipboard.\n')

        print('\n'.join(matches))
        sys.exit(0)

    else:
        print('[-] No phone numbers or email found on clipboard.')
        sys.exit(1)
