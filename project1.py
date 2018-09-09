from pathlib import Path
import os
import shutil
import re
import time
from stat import *

def first_part(): #takes care of input and deciding which path to take
    global rdl
    rdl = []
    while (True):
        userinput = input()
        command = userinput[0]
        userinput = userinput[2:]
        if (command == 'D') & (os.path.exists(userinput) == True) & (os.path.isdir(userinput)):
             return(userinputtedd(userinput))
        elif (command == 'R') & (os.path.exists(userinput) == True) & (os.path.isdir(userinput)):
            originallist = []
            originallist.append(userinput)
            userinputtedr(originallist)
            return rdl
        else:
            print ("ERROR")    

def userinputtedd(root: Path):
    first_result = []
    for each in os.listdir(root):
        new = (root + "/" + each)
        if ((os.path.isfile(new)) & (new.endswith('.DS_Store') == False)):
           first_result.append(new)
    first_result.sort()
    return first_result

def userinputtedr(array: [Path]):
 #   temporaryarray = []
    temporarydirectoryarray = []
    for eachpath in array:
        for temp in os.listdir(eachpath):
            new = (eachpath + "/" + temp)
            if ((os.path.isfile(new)) & (new.endswith('.DS_Store') == False)):
 #               temporaryarray.append(new)
 #               temporaryarray.sort()
                 rdl.append(new)
            elif (os.path.isdir(new)):
                temporarydirectoryarray.append(new)
                temporarydirectoryarray.sort()
        if not (len(temporarydirectoryarray) == 0):
            rdl.sort()
            userinputtedr(temporarydirectoryarray)

def second_part(files: [Path]):
    interesting_files = []
    while (True):
        userinput = input().strip()
        command = userinput[0]
        if command == 'A':
            for i in range(len(files)):
                interesting_files.append(files[i])
            interesting_files.sort()
            return interesting_files
        elif ((command == 'N') & (len(userinput) >= 2)):
            userinput = userinput[2:].strip()
 #           print (files)
            for each in files:
                if os.path.basename(each) == userinput:
                    interesting_files.append(each)
 #               interesting_files.sort()
            return interesting_files
        elif ((command == 'E') & (len(userinput) >= 2)):
            userinput = userinput[2:].strip()
            for each in files:
                if each.endswith(userinput):
                    interesting_files.append(each)
 #           interesting_files.sort()
            return interesting_files
        elif ((command == 'T') & (len(userinput) >= 2)):
            userinput = userinput[2:].strip()
            for each in files:
                if (os.access(userinput, os.R_OK) == True):
                    temp = open(each, 'r')
                    for line in temp.read():
                        if (userinput) in line:
                            interesting_files.append(each)
            interesting_files.sort()
            return interesting_files
        elif ((command == '<') & (len(userinput) >= 2)):
            userinput = userinput[2:].strip()
            for each in files:
                if (os.path.getsize(each)) < int(userinput):
                        interesting_files.append(each)
            interesting_files.sort()
            return interesting_files
        elif ((command == '>') & (len(userinput) >= 2)):
            userinput = input[2:]
            for each in files:
                if (os.path.getsize(each)) > int(userinput):
                    interesting_files.append(each)
            interesting_files.sort()
            return interesting_files
        else:
            print("ERROR")

def third_part(files: [Path]):
    if (len(files) == 0):
        quit()      
    while (True):
        command = input()
        if command == 'F':
            for i in range(len(files)):
                if files[i].endswith('.txt'):
                    first = open(files[i], 'r')
                    second = first.readline()
                    second = second.rstrip('\n')
                    print(second)
                else:
                    print ("NOT TEXT")
            break
        elif command == 'D':
            for i in range(len(files)):
                head, tail = path.split(files[i])
                duplicate_path = files[i] + ".dup"
                shutil.copy(files[i], duplicate_path)
                shutil.copystat(files[i], duplicate_path)
            break
        elif command == 'T':
            for i in range(len(files)):
                st = os.stat(files[i])
                original = st[ST_ATIME]
                duplicate = st[ST_MTIME]
                os.utime(files[i], (original, duplicate))
        else:
            print ("ERROR")

    quit()
fdirname = first_part()
for i in range(len(fdirname)):
    print (fdirname[i])
sdirname = second_part(fdirname)
for i in range(len(sdirname)):
    print (sdirname[i])
third_part(sdirname)
quit()


        
