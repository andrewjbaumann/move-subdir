'''
@author abaumann 
'''

import shutil 
from glob import glob

starting_dir = raw_input("What is the grandparent directory?")
dirlist = list()
dirlist = glob("..\\"+ starting_dir + "*")

print dirlist

for subdirs in dirlist:
	shutil.copytree(subdirs, "..\\")