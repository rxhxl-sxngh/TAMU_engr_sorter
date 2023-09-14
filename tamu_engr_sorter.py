import os
from pathlib import Path
import shutil
# from sre_constants import SUCCESS
# from typing import final

downloads_path = str(Path.home() / "Downloads/")
final_path = r"C:\Documents\TAMU"
entries = os.listdir(downloads_path)
destination = os.listdir(final_path)
not_selected = []

CSCE121 = "CSCE121"
CSCE222 = "CSCE222"
MEEN431 = "MEEN431"
MEEN439 = "MEEN439"
MEEN459 = "MEEN459"
MEEN464 = "MEEN464"
MEEN210 = "MEEN210"

for entry in entries:
    if entry.find(MEEN401) != -1:

        for dst in destination:
            if dst == MEEN401:
                source = (downloads_path + "\\" + entry) 
                end_source = (final_path + "\\" + dst) 
                shutil.copy2(source, end_source)
                os.remove(source)


    if entry.find(MEEN404) != -1:
        print(entry)

        for dst in destination:
            if dst == MEEN404:
                source = (downloads_path + "\\" + entry) 
                end_source = (final_path + "\\" + dst) 
                shutil.copy2(source, end_source)
                os.remove(source)


    if entry.find(MEEN431) != -1:
        print(entry)

        for dst in destination:
            if dst == MEEN431:
                source = (downloads_path + "\\" + entry) 
                end_source = (final_path + "\\" + dst) 
                shutil.copy2(source, end_source)
                os.remove(source)


    if entry.find(MEEN439) != -1:
        print(entry)   

        for dst in destination:
            if dst == MEEN439:
                source = (downloads_path + "\\" + entry) 
                end_source = (final_path + "\\" + dst) 
                shutil.copy2(source, end_source)
                os.remove(source)


    if entry.find(MEEN459) != -1:
        print(entry)

        for dst in destination:
            if dst == MEEN459:
                source = (downloads_path + "\\" + entry) 
                end_source = (final_path + "\\" + dst) 
                shutil.copy2(source, end_source)
                os.remove(source)


    if entry.find(MEEN464) != -1:
        print(entry)

        for dst in destination:
            if dst == MEEN464:
                source = (downloads_path + "\\" + entry) 
                end_source = (final_path + "\\" + dst) 
                shutil.copy2(source, end_source)
                os.remove(source)
                
    if entry.find(MEEN210) != -1:
        print(entry)

        for dst in destination:
            if dst == MEEN210:
                source = (downloads_path + "\\" + entry) 
                end_source = (final_path + "\\" + dst) 
                shutil.copy2(source, end_source)
                os.remove(source)
    else:
        not_selected.append(entry)
