# file organizer project 

import os
import shutil

path = r"C:\Users\karth\Downloads\Os module"

files_exist = os.listdir(path) 
print(files_exist)

Folders_create = ["Image's", "Video's", "document's","script's", "audio's"]

for folders in Folders_create:
    if not os.path.exists(os.path.join(path,folders)):
        os.makedirs(os.path.join(path,folders))
    else:
        print(f"{folders} folder already exists")

document_ext = [".pdf", ".ppt", ".pptx", ".doc", ".docx", ".xls", ".xlsx",".csv", ".txt"]

image_ext = [".png", ".jpg", ".jpeg", ".gif"]

video_ext = [".mp4", ".mkv", ".avi"]

script_ext = [".py", ".js", ".html", ".css"]

audio_ext = [".mp3", ".wav", ".aac"]

for file in files_exist:

    source = os.path.join(path, file)

    if os.path.isdir(source):
        continue

    name, ext = os.path.splitext(file)
    ext = ext.lower()

    if ext in document_ext:
        destination = os.path.join(path,"document's",file)
        shutil.move(source, destination)
        print(f"{file} moved to document's folder")

    elif ext in image_ext:
        destination = os.path.join(path,"Image's",file)
        shutil.move(source, destination)
        print(f"{file} moved to Image's folder")

    elif ext in video_ext:
        destination = os.path.join(path,"Video's",file)
        shutil.move(source, destination)
        print(f"{file} moved to Video's folder")

    elif ext in script_ext:
        destination = os.path.join(path,"script's",file)
        shutil.move(source, destination)
        print(f"{file} moved to script's folder")

    elif ext in audio_ext:
        destination = os.path.join(path,"audio's",file)
        shutil.move(source, destination)
        print(f"{file} moved to audio's folder")

