#!/usr/bin/env python

import argparse, os, magic

from shutil import copyfile

parser = argparse.ArgumentParser()

#-extract /User/some/directory/destination
parser.add_argument("-e", "--extract", help="Full Directory Path e.g. '/Users/some/directory/destination'")

args = parser.parse_args()

def extract():
    print('Intializing restore.....')
    error_count = 0
    extracted = "restored"
    print('creating restore folder.....')
    try:
        os.makedirs(extracted)
    except:
        print(f'{extracted} folder found')
        pass
    backup_folder = args.extract
    '''
    itunes backup folder looks like this:
    
    backup_folder/
                folder/
                    file, file, file
                folder/
                    file, file, file
                folder/
                    file, file, file
    '''
    if backup_folder:
        print('Checking backup folder.....')
        for folder in os.listdir(backup_folder):
            '''
            get a list of everything in the backup_folder
            and identify directories
            '''
            path = f"{backup_folder}/{folder}"
            print(f"Found {path}")
            if os.path.isdir(path):
                print(f"Looking for files from {path}")
                '''
                go through all files in the folder
                '''
                for _file in os.listdir(path):
                    '''
                    ignore if hidden files
                    '''
                    file_path = f"{path}/{_file}"
                    if not _file.startswith('.') and not os.path.isdir(file_path):
                        print(f"Found {_file}")
                        _type = magic.from_file(file_path, mime=True)
                        # _types: (image/png, None)
                        extension = _type.split('/')[1]
                        corrected_file = f"{_file}.{extension}"
                        # corrected_file: file.ext
                        # copyfile(src, dst)
                        new_file = f"{extracted}/{corrected_file}"
                        # new_file: restored/file.ext
                        print(f"{_file} has been restored to {corrected_file}")
                        try:
                            copyfile(file_path, new_file)
                        except Exception as e:
                            print(e)
                            error_count+=1
                            pass
    errors = f" However there were {error_count} errors encountered." if error_count else ""
    report = f"Your files have been extracted and copied to the restored folder.{errors}" if backup_folder else "Ensure you pass proper backup folder location"
    print(report)