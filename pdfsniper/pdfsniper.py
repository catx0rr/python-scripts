#!/usr/bin/python3

'''
    pdfsniper.py - PDF to text. 

    | EXTRACT | CRACK | ENCRYPT | READ
    
    Author: catx0rr

    SEE: Usage below.

    !! DEPENDECIES !!
    pdfsniper pdftotext module:
        Linux: libpoppler
               - sudo apt-get install libpoppler-cpp-dev
        Windows: Microsoft Visual C++ 14.0
               - Get it with "Microsoft Visual C++ Build Tools": https://visualstudio.microsoft.com/downloads/

    !! ISSUES !!
    Decrypt option: Some of encryption algorithm is not supported as per PyPDF2
        NotImplementedError: only algorithm code 1 and 2 are supported.

    Note: Tried on some encrypted pdf and used a well known passwordlist, worked as it should be.

    SEE: Issues on these pages.
        github: https://github.com/mstamy2/PyPDF2/issues/53
                https://github.com/mstamy2/PyPDF2/issues/378

        stackoverflow:
                https://stackoverflow.com/questions/50751267/only-algorithm-code-1-and-2-are-supported


    !! DOCUMENTATIONS !!
        PyPDF2: https://pythonhosted.org/PyPDF2/PdfFileReader.html
        pdftotext: https://pypi.org/project/pdftotext/
'''

import getpass
import pdftotext
import PyPDF2
import re
import sys

file_gex = re.compile(r'[a-zA-Z0-9._-]+\.[a-zA-Z]')

usage = '''[>] Usage: pdf_extract.py [option] [pdffile] [option]

help                    -- Shows the usage.
count                   -- Count the number of pages the targeted pdf file.
read [int]              -- Read the pdf page in the terminal. Fourth argument required as page index of 0.
readall                 -- Print all page contents of the pdf file in the terminal.
extract                 -- Extracts the pdf texts and output it in a text file.
checkcrypt              -- Checks if file.pdf is encrypted.
binextract              -- Extracts the pdf and write the binary file in a text file.
encrypt                 -- Encrypts unencrypted pdf with a desired password.
decrypt [passwd_file]   -- Decrypts the file using a password list as fourth argument passed.'''


def count(file):

    # read pdf, read as binary ('rb') and output how many pages
    try:
        with open(file, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfFileReader(pdf_file)
            print('[+] %s page(s) count: %s' % (file, pdf_reader.numPages))

        pdf_file.close()

    except PyPDF2.utils.PdfReadError:
        print('[-] Unable to count %s Please check if the file is encrypted.' % (file))

    except FileNotFoundError:
        print('[-] %s not found.' % (file))


def read(file, page):

    try:
        with open(file, 'rb') as pdf_file:
            pdf_reader = pdftotext.PDF(pdf_file)

            print(pdf_reader[page])

        pdf_file.close()

    except pdftotext.Error:
        print('[-] Unable to read %s Please check if the file is encrypted.' % (file))

    except FileNotFoundError:
        print('[-] %s not found.' % (file))


def read_all(file):

    try:
        with open(file, 'rb') as pdf_file:
            pdf_reader = pdftotext.PDF(pdf_file)

            # Iterate over the pages and print on the terminal
            for pdf_page in pdf_reader:
                print(pdf_page)

        pdf_file.close()

    except pdftotext.Error:
        print('[-] Unable to read %s Please check if the file is encrypted.' % (file))

    except FileNotFoundError:
        print('[-] %s not found.' % (file))


def extract(file):

    name_text = file.replace('.pdf', '.txt')

    print('[*] Working on %s pdf file..' % (file))

    try:
        with open(file, 'rb') as pdf_file, open(name_text, 'a') as text_file:
            pdf_reader = pdftotext.PDF(pdf_file)

            # Iterate and write on a file
            for pdf_page in pdf_reader:
                text_file.write(pdf_page + '\n\n---------------//  P A  G  E    B  R  E  A  K  //---------------\n\n')

        pdf_file.close()
        text_file.close()
        print('[+] %s has been extracted to %s.' % (sys.argv[2], name_text))

    except pdftotext.Error:
        print('[-] Unable to extract %s Please check if the file is encrypted.' % (file))

    except FileNotFoundError:
        print('[-] %s not found.' % (file))


def check_crypt(file):

    try:
        with open(file, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfFileReader(pdf_file)

            if pdf_reader.isEncrypted:
                print('[+] %s is password protected.' % (file))

            else:
                print('[+] %s is not encrypted.' % (file))

        pdf_file.close()

    except FileNotFoundError:
        print('[-] %s not found.' % (file))


def bin_extract(file):

    name_text = file.replace('.pdf', '_bin.txt')

    print('[*] Working on %s pdf file..' % (file))

    # Extracts the binary target pdf file and output it into a text file.

    try:
        with open(file, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfFileReader(pdf_file)

            # Create an writer object to add pages of current pdf file
            pdf_writer = PyPDF2.PdfFileWriter()

            # iterate on the pages of current pdf file
            for page_num in range(pdf_reader.numPages):
                page_object = pdf_reader.getPage(page_num)

                pdf_writer.addPage(page_object)

        # Create a empty text file and write the pages from current pdf file
        with open(name_text, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)
            print('[+] %s extracted to %s file.' % (sys.argv[2], name_text))

        output_pdf.close()
        pdf_file.close()

    except PyPDF2.utils.PdfReadError:
        print('[-] Unable to extract %s Please check if the file is encrypted.' % (file))

    except FileNotFoundError:
        print('[-] %s not found.' % (file))


def decrypt(file, passwd_file):

    # Open the pdf file and the password file and check for passwords inside

    try:
        pdf_reader = PyPDF2.PdfFileReader(open(file, 'rb'))
        with open(passwd_file, 'r') as pass_file:

            # Iterate in every line of the opened password list and list the index and the password if found.
            for index, line in enumerate(pass_file):

                password = line.strip()
                if pdf_reader.decrypt(password) == 1:
                    pass_found = password
                    print('[+] Line: %s Password found: %s' % (index, pass_found))
                    break

                else:
                    print('[-] Line: %s No match found. yet..' % (index))

        pass_file.close()

    except KeyError:
        print('[-] %s not encrypted.' % (file))

    except FileNotFoundError:
        print('[-] PDF or password file not found.')

    except NotImplementedError:
        print('[-] Password Hash not supported. "only algorithm code 1 and 2 are supported" Please see issues.')


def encrypt(file, password):
    try:

        name_pdf = file.replace('.pdf', '_encrypted.pdf')

        # Load the pdf writer and reader
        pdf_reader = PyPDF2.PdfFileReader(file)
        pdf_writer = PyPDF2.PdfFileWriter()
        pdf_pages = pdf_reader.getNumPages()

        print('[*] Working on %s pdf file..' % (file))

        # Get the page of loaded pdf file
        for page in range(pdf_pages):
            pdf_writer.addPage(pdf_reader.getPage(page))

        # Encrypt the password with the passed argument
        pdf_writer.encrypt(user_pwd=password, owner_pwd=None, use_128bit=True)

        # Output the encrypted product pdf
        with open(name_pdf, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)

        output_pdf.close()
        print('[+] Done. %s saved on current working directory.' % (name_pdf))

    except PyPDF2.utils.PdfReadError:
        print('[-] Unable to encrypt %s You cannot encrypt an unencrypted file.' % (file))

    except FileNotFoundError:
        print('[-] %s not found.' % (file))

def pass_gen():

    while True:
        passwd = getpass.getpass('[>] Enter password: ')
        re_passwd = getpass.getpass('[>] Confirm password: ')

        if not passwd:
            print('[-] Password must not be empty.')
            continue

        if not re_passwd:
            print('[-] Password must not be empty.')
            continue

        if passwd == re_passwd:
            if len(passwd) < 4:
                print('[-] Password must be at least 4 characters.')
                continue

            return passwd
            break

        else:
            print('[-] Passwords did not match.')


def check_pwfile(pwfile):
    try:
        if file_gex.search(pwfile).group():
            return pwfile

    except AttributeError:
        print('[-] Invalid password file.')
        sys.exit(1)


def check_page(pagenum):
    if pagenum.isdigit():
        return int(pagenum)

    else:
        print(usage)
        sys.exit(1)


if __name__ == '__main__':

    if len(sys.argv) < 2:
        print(usage)
        sys.exit(1)

    elif len(sys.argv) == 2 and sys.argv[1] == 'help':
        print(usage)
        sys.exit(0)

    elif len(sys.argv) == 3 and sys.argv[1] == 'count':
        count(sys.argv[2])
        sys.exit(0)

    elif len(sys.argv) == 4 and sys.argv[1] == 'read' and sys.argv[3] != '':
        read(sys.argv[2], check_page(sys.argv[3]))
        sys.exit(0)

    elif len(sys.argv) == 3 and sys.argv[1] == 'extract':
        extract(sys.argv[2])
        sys.exit(0)

    elif len(sys.argv) == 3 and sys.argv[1] == 'readall':
        read_all(sys.argv[2])
        sys.exit(0)

    elif len(sys.argv) == 3 and sys.argv[1] == 'checkcrypt':
        check_crypt(sys.argv[2])
        sys.exit(0)

    elif len(sys.argv) == 3 and sys.argv[1] == 'binextract':
        bin_extract(sys.argv[2])
        sys.exit(0)

    elif len(sys.argv) == 4 and sys.argv[1] == 'decrypt':
        decrypt(sys.argv[2], check_pwfile(sys.argv[3]))
        sys.exit(0)

    elif len(sys.argv) == 3 and sys.argv[1] == 'encrypt':
        encrypt(sys.argv[2], pass_gen())
        sys.exit(0)

    else:
        print(usage)
        sys.exit(0)
