#!/usr/bin/python3

'''
    back_to_zip.py
    - Copies an entire directory and contents and back up your files with zip.

'''
import time
import os
import sys
import zipfile


err = r'''[-] Usage: back_to_zip.py [path]
Examples:
back_to_zip.py C:\Users\username\Desktop\my_directory_backup'''


def backup_to_zip(directory):
    # Back up the entire contents of the directory into a zip file

    directory = os.path.abspath(directory)     # get the pwd using absolute path

    # Check the filename what files already exist.
    # Will increment the name backup in order not to overwrite

    number = 1

    while True:
        zipfile_name = os.path.basename(directory) + '_' + str(number) + '.zip'
        if not os.path.exists(zipfile_name):
            break
        number += 1

    # Create a zip file backup
    print('[>] Creating %s...' % (zipfile_name))
    time.sleep(2)

    with zipfile.ZipFile(zipfile_name, 'w') as backup_zip:

        # Walk the entire directory tree and compress the files in each directory.
        for directory_name, sub_directory, file_names in os.walk(directory):
            print('[+] Adding files in %s...' % (directory_name))
            time.sleep(1)

            # Add the current directory to the zip file.
            backup_zip.write(directory_name)

            # Add all the files in this directory to the zip file
            for file_name in file_names:
                new_base = os.path.basename(directory) + '_'

                if file_name.startswith(new_base) and file_name.endswith('.zip'):
                    continue    # don't backup the backup zip files

                backup_zip.write(os.path.join(directory_name, file_name))

        backup_zip.close()
        print('[+] Done..')


if __name__ == '__main__':

    if len(sys.argv) < 2 or len(sys.argv) > 2:
        print(err)
        sys.exit(1)

    else:
        backup_to_zip(sys.argv[1])
        sys.exit(0)
