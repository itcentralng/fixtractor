#!/usr/bin/env python

import argparse, os, magic

from shutil import copyfile

parser = argparse.ArgumentParser()

#-extract /User/some/directory/destination
parser.add_argument("-e", "--extract", help="Full Directory Path e.g. '/Users/some/directory/destination'")
parser.add_argument("-m", "--minimum", nargs='?', default="0mb", help="Minimum file size e.g. '2mb'")

args = parser.parse_args()

restore_folder = "restored"
error_count = 0
success_count = 0

def minimum_size():
    minimum = args.minimum.lower()
    kb = 1042
    mb = kb**2
    gb = kb**3
    tb = kb**4
    if 'kb' in minimum:
        minimum = minimum.split('kb')[0].strip()
        size = int(minimum) * kb
    elif 'mb' in minimum:
        minimum = minimum.split('mb')[0].strip()
        size = int(minimum) * mb
    elif 'gb' in minimum:
        minimum = minimum.split('gb')[0].strip()
        size = int(minimum) * gb
    elif 'tb' in minimum:
        minimum = minimum.split('tb')[0].strip()
        size = int(minimum) * tb
    return size

def go_through(folder):
    for content in os.listdir(folder):
        path = f"{folder}/{content}"
        if os.path.isdir(path):
            go_through(path)
        else:
            correct_file(path)

def correct_file(file_path):
    global error_count
    global success_count
    global restore_folder
    if os.stat(file_path).st_size > minimum_size():
        _file = os.path.basename(file_path)
        _type = magic.from_file(file_path, mime=True)
        # _types: image/png
        extension = _type.split('/')[1]
        corrected_file = f"{_file}.{extension}"
        # corrected_file: file.ext
        # copyfile(src, dst)
        new_file = f"{restore_folder}/{corrected_file}"
        # new_file: restored/file.ext
        print(f"{_file} has been restored to {corrected_file}")
        try:
            copyfile(file_path, new_file)
            success_count+=1
        except Exception as e:
            print(e)
            error_count+=1
            pass
    return True

def extract():
    global restore_folder
    print('Intializing restore..')
    print('creating restore folder..')
    try:
        os.makedirs(restore_folder)
    except:
        print(f'{restore_folder} folder found')
        pass
    main_folder = args.extract
    '''
    initial folder assumption:
    
    main_folder/
                -folder/
                    -file
                -file
    '''
    if main_folder:
        print(f'Checking {main_folder}..')
        for content in os.listdir(main_folder):
            '''
            get a list of everything in the main_folder
            and identify directories and files but ignore hidden files
            '''
            if not content.startswith('.'):
                path = f"{main_folder}/{content}"
                if os.path.isdir(path):
                    go_through(path)
                else:
                    correct_file(path)
    errors = f" However there were {error_count} errors encountered." if error_count else ""
    report = f"Your files have been extracted and copied to the {restore_folder} folder.{errors}" if main_folder else "Ensure you pass proper backup folder location"
    print(report)
    return {'success':success_count, 'error':error_count}