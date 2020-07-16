#!/usr/bin/env python

import argparse, os, mimetypes

from shutil import copyfile

parser = argparse.ArgumentParser()

#-extract /User/some/directory/destination
parser.add_argument("-e", "--extract", help="Full Directory Path e.g. '/Users/some/directory/destination'")

args = parser.parse_args()

def extract():
    error_count = 0
    extracted = "restored"
    os.makedirs(extracted)
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
        for folder in os.listdir(backup_folder):
            '''
            get a list of everything in the backup_folder
            and identify directories
            '''
            path = f"{backup_folder}/{folder}"
            if os.path.isdir(path):
                '''
                go through all files in the folder
                '''
                for _file in path:
                    '''
                    ignore if hidden files
                    '''
                    if not _file.startswith('.'):
                        file_path = f"{path}/{_file}"
                        _type = mimetypes.guess_type(file_path)
                        # _types: (image/png, None)
                        extension = _type[0].split('/')[1]
                        corrected_file = f"{_file}.{extension}"
                        # corrected_file: file.ext
                        # copyfile(src, dst)
                        new_file = f"{extracted}/{corrected_file}"
                        # new_file: restored/file.ext
                        try:
                            copyfile(corrected_file, new_file)
                        except Exception as e:
                            print(e)
                            error_count+=1
                            pass
    errors = f" However there were {error_count} errors encountered." if error_count else ""
    report = f"Your files have been extracted and copied to the restored folder.{errors}" if backup_folder else "Ensure you pass proper backup folder location"
    print(report)