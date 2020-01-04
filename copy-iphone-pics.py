# import modules
import exifread
import os
import logging
import datetime
from pathlib import Path
from shutil import copyfile
logging.getLogger("exifread").setLevel(logging.WARNING)
# 
# Create list of months 
monthList = {}
monthList['01'] = 'Jan'
monthList['02'] = 'Feb'
monthList['03'] = 'Mar'
monthList['04'] = 'Apr'
monthList['05'] = 'May'
monthList['06'] = 'Jun'
monthList['07'] = 'Jul'
monthList['08'] = 'Aug'
monthList['09'] = 'Sep'
monthList['10'] = 'Oct'
monthList['11'] = 'Nov'
monthList['12'] = 'Dec'
# Specify source path iCloud photos download directory)
sourcePath = Path(r"C:\Users\Michael\Pictures\iCloud Photos\Downloads")
# Specify destination path 
destPathParent = Path(r"C:\Users\Michael\Pictures")
# Loop through files in source directory
for filename in os.listdir(sourcePath):
    # If file is a image, process it
    print(f"Now examining {filename}")
    if (filename.endswith('.jpg') or filename.endswith('.JPG')): 
        fullSourceName = sourcePath / filename
        with open("%s/%s" % (sourcePath, filename), 'rb') as image: # file path and name
            exif_tags = exifread.process_file(image, stop_tag='DateTimeOriginal')
            #
            # if the file is a photo (i.e, has an EXIF DateTimeOriginal tag), copy it           
            if 'EXIF DateTimeOriginal' in exif_tags:
                #
                t = str(exif_tags['EXIF DateTimeOriginal'])
                t = t.replace(" ", ":")
                tp = t.split(':')
                monString = tp[1] + "-" + monthList[tp[1]]
                destPath = destPathParent / tp[0] / monString / tp[2]
                fullDestName = destPath / filename 
                # if the destination directory (\yyyy\mm mon\dd) does not exist, create it
                if not os.path.isdir(destPath):
                    os.mkdir(destPath)
                    # 
                    print(f"Created {destPath} ")
                # Does file already exist in destination directory? 
                #    If yes, skip
                #    If no, copy
                if not os.path.isfile(fullDestName):
                      copyfile(fullSourceName, fullDestName)
                      # 
                      print(f"Copied {fullSourceName} to {fullDestName} ")
            