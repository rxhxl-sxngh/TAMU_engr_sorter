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

ENGR102 = "ENGR102"
ENGR216 = "ENGR216"
CSCE121 = "CSCE121"
CSCE222 = "CSCE222"
CSCE221 = "CSCE221"
CSCE312 = "CSCE312"
CSCE314 = "CSCE314"
MATH151 = "MATH151"
MATH152 = "MATH152"
MATH251 = "MATH251"
MATH304 = "MATH304"
MATH308 = "MATH308"
CSCE313 = "CSCE313"
CSCE315 = "CSCE315"
CSCE411 = "CSCE411"


for entry in entries:
    if entry.find(ENGR102) != -1:

        for dst in destination:
            if dst == ENGR102:
                source = (downloads_path + "\\" + entry) 
                end_source = (final_path + "\\" + dst) 
                shutil.copy2(source, end_source)
                os.remove(source)


    if entry.find(ENGR216) != -1:
        print(entry)

        for dst in destination:
            if dst == ENGR216:
                source = (downloads_path + "\\" + entry) 
                end_source = (final_path + "\\" + dst) 
                shutil.copy2(source, end_source)
                os.remove(source)


    if entry.find(CSCE121) != -1:
        print(entry)

        for dst in destination:
            if dst == CSCE121:
                source = (downloads_path + "\\" + entry) 
                end_source = (final_path + "\\" + dst) 
                shutil.copy2(source, end_source)
                os.remove(source)


    if entry.find(CSCE222) != -1:
        print(entry)   

        for dst in destination:
            if dst == CSCE222:
                source = (downloads_path + "\\" + entry) 
                end_source = (final_path + "\\" + dst) 
                shutil.copy2(source, end_source)
                os.remove(source)


    if entry.find(CSCE221) != -1:
        print(entry)

        for dst in destination:
            if dst == CSCE221:
                source = (downloads_path + "\\" + entry) 
                end_source = (final_path + "\\" + dst) 
                shutil.copy2(source, end_source)
                os.remove(source)


    if entry.find(CSCE312) != -1:
        print(entry)

        for dst in destination:
            if dst == CSCE312:
                source = (downloads_path + "\\" + entry) 
                end_source = (final_path + "\\" + dst) 
                shutil.copy2(source, end_source)
                os.remove(source)
                
    if entry.find(CSCE314) != -1:
        print(entry)

        for dst in destination:
            if dst == CSCE314:
                source = (downloads_path + "\\" + entry) 
                end_source = (final_path + "\\" + dst) 
                shutil.copy2(source, end_source)
                os.remove(source)

    if entry.find(MATH151) != -1:
        print(entry)

        for dst in destination:
            if dst == MATH151:
                source = (downloads_path + "\\" + entry) 
                end_source = (final_path + "\\" + dst) 
                shutil.copy2(source, end_source)
                os.remove(source)

    if entry.find(MATH152) != -1:
        print(entry)

        for dst in destination:
            if dst == MATH152:
                source = (downloads_path + "\\" + entry) 
                end_source = (final_path + "\\" + dst) 
                shutil.copy2(source, end_source)
                os.remove(source)

    if entry.find(MATH251) != -1:
        print(entry)

        for dst in destination:
            if dst == MATH251:
                source = (downloads_path + "\\" + entry) 
                end_source = (final_path + "\\" + dst) 
                shutil.copy2(source, end_source)
                os.remove(source)

    if entry.find(MATH304) != -1:
        print(entry)

        for dst in destination:
            if dst == MATH304:
                source = (downloads_path + "\\" + entry) 
                end_source = (final_path + "\\" + dst) 
                shutil.copy2(source, end_source)
                os.remove(source)

    if entry.find(MATH308) != -1:
        print(entry)

        for dst in destination:
            if dst == MATH308:
                source = (downloads_path + "\\" + entry) 
                end_source = (final_path + "\\" + dst) 
                shutil.copy2(source, end_source)
                os.remove(source)

    if entry.find(CSCE313) != -1:
        print(entry)

        for dst in destination:
            if dst == CSCE313:
                source = (downloads_path + "\\" + entry) 
                end_source = (final_path + "\\" + dst) 
                shutil.copy2(source, end_source)
                os.remove(source)

    if entry.find(CSCE315) != -1:
        print(entry)

        for dst in destination:
            if dst == CSCE315:
                source = (downloads_path + "\\" + entry) 
                end_source = (final_path + "\\" + dst) 
                shutil.copy2(source, end_source)
                os.remove(source)

    if entry.find(CSCE411) != -1:
        print(entry)

        for dst in destination:
            if dst == CSCE411:
                source = (downloads_path + "\\" + entry) 
                end_source = (final_path + "\\" + dst) 
                shutil.copy2(source, end_source)
                os.remove(source)

    
    else:
        not_selected.append(entry)
