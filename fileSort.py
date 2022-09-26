'''
File Sorter for videos and audio; sorts by the creation date found in the metadata of the video; separates audio files to their own folder. Change the directory to video folder path. Next implementations will be extension dictionary and config file for directory.
'''
__author__ = "Jacob Emmerson"
import os
import time
import shutil

def fileSort(directory):
    #for every file in the scanned directory (desktop)
    for files in os.scandir(directory): #gets iterator of DirEntry objects
        if files.is_file(): #check if current 'files' not a dir
            if files.path.endswith('.mp4') or files.path.endswith('.mkv'): #if file is a video
                fileTime = time.ctime(os.path.getctime(files.path))
                fileName = fileTime[4:7] + fileTime[19:24]
                tempPath = directory + "\\" + fileName
                if os.path.exists(tempPath): #if dir of date exists...
                    shutil.move(files.path, tempPath) #moves file to dir

                else:
                    os.mkdir(tempPath) #else make dir...
                    print("Creating folder " + fileName + "...")
                    shutil.move(files.path, tempPath)

            elif files.path.endswith('.mp3') or files.path.endswith('.wav'): #if an audio file...
                tempPath = directory + "\\Audio"
                if os.path.exists(tempPath): #if audio dir exists...
                    shutil.move(files.path, tempPath)

                else:
                    os.mkdir(tempPath)
                    print("Creating Audio Folder...")
                    shutil.move(files.path, tempPath)

def main():
    #path to desktop
    directory = r"C:\Users\emmer\Desktop"

    fileSort(directory)
    
if __name__ == "__main__":
    main()