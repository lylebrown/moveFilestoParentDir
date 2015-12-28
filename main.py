import os
import shutil
import re


def hasTrackNum(filename):
    return bool(re.search(r'^\d\d -', filename))

basePath = "I:\\Music"
artistList = []
for subdir, dirs, files in os.walk(basePath):
    artistList.append(dirs)

for artist in artistList[0]:
    for subdir, dirs, files in os.walk((basePath + "\\" + artist)):
        albumDir = ""
        if subdir != (basePath + "\\" + artist):
            albumDir = subdir
        if albumDir != "":
            for file in os.listdir(albumDir):
                origFileName = albumDir + "\\" + file
                if hasTrackNum(file) and albumDir.split("\\")[-1] != "Unknown Album":
                    newFileName = os.path.realpath(albumDir + "\\" + file + "\\..\\..") + "\\" + albumDir.split("\\")[-1] + " " + file[0:2] + " - " + file[5:]
                elif not hasTrackNum(file) and albumDir.split("\\")[-1] != "Unknown Album":
                    newFileName = os.path.realpath(albumDir + "\\" + file + "\\..\\..") + "\\" + albumDir.split("\\")[-1] + " - " + file
                else:
                    if hasTrackNum(file):
                        newFileName = os.path.realpath(albumDir + "\\" + file + "\\..\\..") + "\\" + file[5:]
                    else:
                        newFileName = os.path.realpath(albumDir + "\\" + file + "\\..\\..") + "\\" + file
                print("Old: ", origFileName,
                      "\nNew: ", newFileName, "\n")
                shutil.move(origFileName, newFileName)
            os.rmdir(albumDir)
