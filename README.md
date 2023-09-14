# TAMU_engr_sorter

# File Organizer

## Overview
This Python script is a directory management system that helps me keep my files organized by moving them from my Downloads folder to specific destination folders within my `C:\Documents\TAMU` directory. The organization is based on predefined keywords associated with different courses. My hope is that fellow aggies use this script to help themselves save time, because I know I do as my TAMU folder has grown incredibly large as CS student. The script has been integrated with my Task Scheduler to run constantly and automatically update my Downloads folder as soon as files are renamed or added.

## Features
- Automatically detects and organizes files from the Downloads folder.
- Moves files to corresponding course-specific folders based on predefined keywords.
- Deletes the original files from the Downloads folder after moving.

## Usage
1. **Clone or Download:** Clone this repository or download the Python script to your local machine.

2. **Configuration:** Open the script in a text editor of your choice. You can modify the script by adding or removing course keywords (`ENGR102`, `ENGR216`, `CSCE121`, etc.) and their associated destination folders.

3. **Run the Script:** Execute the script by running it using a Python interpreter:
   ```shell
   python tamu_engr_sorter.py


You can customize this script by adding more course keywords and their associated destination folders. To do this, simply follow the pattern already established in the script for the existing courses.

if entry.find(COURSE_KEYWORD) != -1:
    for dst in destination:
        if dst == COURSE_KEYWORD:
            # Move and delete the file
            source = (downloads_path + "\\" + entry)
            end_source = (final_path + "\\" + dst)
            shutil.copy2(source, end_source)
            os.remove(source)

## Note
- Please ensure that you have appropriate permissions to access and modify files in your Downloads folder and the `C:\Documents\TAMU` directory.

- Be cautious when modifying the script to avoid unintentional file deletions.

- Always back up important files before running the script.

- This script can be configured to run at scheduled intervals using Task Scheduler to ensure continuous file organization. If you've set up the script in Task Scheduler, it will run automatically as per your scheduled tasks, keeping your files organized without manual intervention.

## Happy organizing!
