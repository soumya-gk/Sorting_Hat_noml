from os import listdir
from os.path import isfile,join
import os

mypath = os.getcwd()
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath,f))]

with open('again','w') as file: 
	for f in onlyfiles:
		file.write(f+'\n')


