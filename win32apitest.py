import string
from time import sleep
from ctypes import windll
import os
import re

#Function to read in the configuration file. If none exists, produce one:
def config():
	try:
		cfg_dict = {}
		cfg_file = open("config.cfg", "r")
		print("Configuration File Found")
		#This will iterate over lines, but not what I want
		for line in cfg_file:
			parameter, values = line.split(' = ')
				#values.remove(value)
		static_drives = values.split(', ')

		#For now, return static drives, elsewise return the entire dictionary
		return cfg_dict

	#If the config file isn't found generate one here
	except FileNotFoundError:
		print("Configuration File Not Found")

		#Read in drive list
		drives = []
		bitmask = windll.kernel32.GetLogicalDrives()
		for letter in string.ascii_uppercase:
			if bitmask & 1:
				drives.append(letter)
			bitmask >>= 1

		#Generate a list of lines to write to the file using writelines()
		#This is okay for the single line config file
		header = "static_drives = "
		parameters = ", ".join(drives)
		parameters = header + parameters
		cfg_file = open("config.cfg", "w+")
		cfg_file.writelines(parameters)
		static_drives = drives

		#For now, just static drives, elsewise entire dictionary used for Config file
		return static_drives


#Function to first get a list of drives attached to the computer, then
#	cleanse the list of 'static' drives
def get_drives():
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    #Is this section comparing the bit output to an ascii 
    for letter in string.ascii_uppercase:
        if bitmask & 1:
            drives.append(letter)
        bitmask >>= 1

    #Cull the 'static' drives listed in config file:
    for i in static_drives:
        if i in drives:
            drives.remove(i) 
    return drives


#if this file was run directly:
if __name__ == '__main__':
	#Preallocate necessary arrays
	old = []
	new = []

	#Run the configuration file stuff here:
	static_drives = config()
	#FOR TESTING: static drives value
	static_drives = ['C', 'D', 'E']

	#Main loop
	while True:
		#Grab connected drive list
		new = get_drives()
		#check if old drifve list is not the same as new drive list
		if old != new:
			print('check it out, new drive')


		#Relist new drives
		old = get_drives()
		print (get_drives())     # On my PC, this prints ['A', 'C', 'D', 'F', 'H']
		#Pause for effect
		sleep(1.5)
	#Using the drive list, cull drives that already showed up