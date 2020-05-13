#!/usr/bin/python3

# index_scraper.py
# scrape domain names in index.html

import re
import sys
from grepfunc import grep


usage = '''[>] Usage: index_scraper.py [index.html]
Example:
index_scraper.py index.html'''

index_regex = re.compile(r'((http|www\.|https)://?[a-zA-Z0-9.-_]+(\.[a-zA-Z]{1,3}))')

# index_regex = re.compile(r'([a-zA-Z0-9_-]+(\.[a-zA-Z]{2,}))')     # without protocol


def print_domain(arg):

    matches, unique = [], []

    try:
        with open(arg, 'r') as f:
            for groups in index_regex.findall(f.read()):
                if groups not in matches:
                    matches.append(groups[0])

                    for uniq in matches:
                        if uniq not in unique:
                            unique.append(uniq)

                    joined = '\n'.join(unique)

        with open('domain.txt', 'w') as g:
            g.write(joined)
            f.close()
            sys.exit(0)

    except FileNotFoundError:
        print(usage, '\n[-] ERROR: File not found.')
        sys.exit(1)


if len(sys.argv) < 2 or len(sys.argv) > 2:
    print(usage)
    sys.exit(1)

else:
    print_domain(sys.argv[1])
    sys.exit(0)
