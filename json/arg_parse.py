#!/usr/bin/python3

import argparse


usage = '''Usage: pdf_extract.py [option] [pdffile] [option]

help                    -- Shows the usage.
count                   -- Count the number of pages the targeted pdf file.
read [int]              -- Read the pdf page in the terminal. Fourth argument required as page index of 0.
readpage                -- Read the pdf per page continuously.
readall                 -- Print all page contents of the pdf file in the terminal.
extract                 -- Extracts all text in the pdf file and output it in a .txt file.
checkcrypt              -- Checks if pdf file is encrypted.
binextract              -- Extracts the pdf and writes all pdf binaries in a text file.
encrypt                 -- Encrypts unencrypted pdf with a desired password.
decrypt [passwd_file]   -- Brute forces and decrypts the file. A password file is needed in fourth argument.
strip                   -- Strips the password on the pdf file. A password is needed in fourth argument.'''


# parser = argparse.ArgumentParser(description='Work with pdf files using the terminal. Extract text files, read continuosly on the page, encrypt files, decrypt and strip the password of the pdf file.')

# parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for the accumulator')
# parser.add_argument('--sum', dest='accumulate', action='store_const', const=sum, default=max,
#                     help='sum the integers (default: find the max)')

# Create a parser for the arguments
# parser = argparse.ArgumentParser(description='Work with pdf files using the terminal. Extract text files, read continuosly on the page, encrypt files, decrypt and strip the password of the pdf file.')

# # Create group of arguments for usage
# group = parser.add_mutually_exclusive_group(required=True)
# group.add_argument('-c', '--count', metavar='', help='Count the number of pages of the selected pdf file.')
# group.add_argument('-r', '--read', nargs=2, metavar='', help='Read and prints the pdf page in the terminal. ')
# group.add_argument('-p', '--read-page', metavar='', help='Creates a session and read the pdf continously on the terminal.')
# group.add_argument('-a', '--read-all', metavar='', help='Read and prints all page content on the terminal.')
# group.add_argument('-x', '--extract', help='Extracts all text in the pdf file and writes it in a .txt file.')
# group.add_argument('-t', '--check-crypt', metavar='', help='Check if the file is encrypted.')
# group.add_argument('-b', '--extract-binary', metavar='', help='Extracts pdf binaries to work with.')
# group.add_argument('-e', '--encrypt', metavar='', help='Encrypts an unencrypted pdf file with a desired password.')
# group.add_argument('-d', '--decrypt', metavar='', nargs=2, help='Performs a brute force attack to the pdf file using a password list.')
# group.add_argument('-s', '--strip', metavar='', help='Strips the password on the pdf file. A password is required.')


# # parser = argparse.ArgumentParser(description='Work with pdf files using the terminal. Extract text files, read continuosly on the page, encrypt files, decrypt and strip the password of the pdf file.')

# # parser.add_argument('-c', '--count', metavar='', dest='count', help='Count the number of pages of the selected pdf file.')
# # parser.add_argument('-r', '--read', metavar='', dest='page', help='Read and prints the pdf page in the terminal.')


# # if args.read is not None:
# argstore = args.read
# args.read = 'reading the page'
# print(args.read, argstore)


def parser():
    parser = argparse.ArgumentParser(
        description='Work with pdf files using the terminal. Extract text files, read continuosly on the page, encrypt files, decrypt and strip the password of the pdf file.',
        allow_abbrev=False
    )

    # Create group of arguments for usage
    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument('-c', '--count', metavar='', help='Count the number of pages of the selected pdf file.')
    group.add_argument('-r', '--read', nargs=2, metavar='', help='Read and prints the pdf page in the terminal. A password is required as fourth argument. ')
    group.add_argument('-p', '--read-page', dest='readpage', metavar='', help='Creates a session and read the pdf continously on the terminal.')
    group.add_argument('-a', '--read-all', dest='readall', metavar='', help='Read and prints all page content on the terminal.')
    group.add_argument('-x', '--extract', metavar='', help='Extracts all text in the pdf file and writes it in a .txt file.')
    group.add_argument('-t', '--check-crypt', dest='checkcrypt', metavar='', help='Check if the file is encrypted.')
    group.add_argument('-b', '--extract-binary', dest='extbinary', metavar='', help='Extracts pdf binaries to work with.')
    group.add_argument('-e', '--encrypt', metavar='', help='Encrypts an unencrypted pdf file with a desired password.')
    group.add_argument('-d', '--decrypt', metavar='', nargs=2, help='Performs a brute force attack to the pdf file using a password list as fourth argument.')
    group.add_argument('-s', '--strip', metavar='', nargs=2, help='Strips the password on the pdf file. A password is required as fourth argument.')

    args = parser.parse_args()

    # Check for options and parsed arguments

    if args.count:
        return args.count

    if args.read:
        return args.read

    if args.readpage:
        return args.readpage

    if args.readall:
        return args.readall

    if args.extract:
        return args.extract

    if args.checkcrypt:
        return args.checkcrypt

    if args.extbinary:
        return args.extbinary

    if args.encrypt:
        return args.encrypt

    if args.decrypt:
        return args.decrypt

    if args.strip:
        return args.strip
