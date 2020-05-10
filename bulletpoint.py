#!/usr/bin/python3

# bulletpoint.py (Advanced)
# Adds bulletpoints every start of new line

import pyperclip
import sys

bullet_name = {
    'star': '*',
    'dash': '-',
    'tilde': '~',
    'plus': '+',
    'colon': ':',
    'equal': '=',
    'arrow': '>'
}

charstring = []

# Function
def bullet_point(string, text):

    # check for string choices
    if choice == "dash":
        out_string = "-"

    elif choice == "star":
        out_string = "*"

    elif choice == "tilde":
        out_string = "~"

    elif choice == "plus":
        out_string = "+"

    elif choice == "colon":
        out_string = ":"

    elif choice == "equal":
        out_string = "="

    elif choice == "arrow":
        out_string = ">"

    else:
        out_string = choice

    # Seperate lines and add stars
    lines = text.split('\n')

    for i in range(len(lines)):                           # loop through all indexes on the list
        lines[i] = f"{out_string} " + lines[i]           # add asterisks in front of every line index

    text = '\n'.join(lines)
    return pyperclip.copy(text)


# Start prompt
print(""" >>> bulletpoint.py <<<
    Usage: Copy first texts and will be converted to bullet pointed format
    Useful in adding bullet points in some sentences / be it email or HTML
      """)

if not pyperclip.paste():
    print("""[-] Copy first texts and will be converted to bullet pointed format:

                 Examples:

                 * Reprehenderit aute voluptate dolore et qui laborum
                 * Excepteur qui officia ut non aute ut labore do sint non.
                 * Lorem ipsum sit ut dolore.
                 * Ex enim aute ut sit elit et eiusmod mollit tempor est consequat laboris.
          """)


while True:
    choice = input("[>] What bullet pointer do you want? [ */-/~/+/:/>/= ]: ")
    err = "[-] Kindly choose bullet points above."

    if not choice.isdigit():
        for key, value in bullet_name.items():
            charstring.append(value)

        if choice in bullet_name or choice in charstring:
            text = pyperclip.paste()
            bullet_point(choice, text)
            print("[+] Output saved to clipboard.")
            sys.exit(0)

        else:
            print(err)

    else:
        print(err)
