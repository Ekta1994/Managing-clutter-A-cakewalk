"""
Please see the paths mentioned in the above post are according to my system, 
we change change paths according to our requirements and do the classification, 
but the important point is then changing the current working directory which is done using os.chdir().
 Also, more if statements can be added pertaining to different file types.
"""

import os
import shutil

filename =  r'c:/Users/Eku/Desktop/Mixed/Images/'

if os.path.exists(filename):
 print "Yes, Image folder exists"  # checking if the image folder exists or not
else:
 print "No, it doesnot exists "                 # if it doesnot, we create the one
 print "Creating a new directory for Images"
 os.makedirs(filename)
 
filename1 = r'c:/Users/Eku/Desktop/Mixed/'

os.chdir(filename1)
 
for file in os.listdir(filename1):   # scannign this drectory for all the files with extension .jpg, i.e. ones that are images 
 if file.endswith(".JPG"):          
  #print file
  shutil.move(file,filename)         # moving them to the image folder
  
filename = r'c:/Users/Eku/Desktop/Mixed/Songs/'

if os.path.exists(filename):         # doing the same like above for songs folder
 print "Yes, songs folder exists"
else:
 print "Songs folder doesnot exists"
 print "Creating new directory for Songs"
 os.makedirs(filename)
 
 
filename1 = r'c:/Users/Eku/Desktop/Mixed'

os.chdir(filename1)

for file in os.listdir(filename1):
 if file.endswith(".mp3"):
  #print file
  shutil.move(file,filename)
