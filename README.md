# Drive_Copy
A python script to automatically copy removable drives to a destination folder with rename/source deletion capabilities

This script is intended to automatically copy drives as they are plugged in.

Requirements: Python 3.7, 

# Planned functionality:
On first run: If no configuration file is found, the script generates a configuration file that records all currently connected drives. Then, the script will prompt a path to the primary repository, and use this information to generate a configuration file that contains the pointer to the desired backup folder and the list of drives to ignore for automatic backup

When the script is run: As removable drives are plugged in, the script will detect that a drive has been added, check the available space on the destination drive and compare it to the used space on the removable drive. Then if the space of the destination is larger, the script will automatically copy the files from the removable drive, verify that the copy is finished and the files are in tact (via comparing exact file size) and if the copy has occurred, the script will automatically delete the source file and throw a message that the drive is safe to remove. 

If the destination drive is full or the removable dive is empty, the script will provide a message (popup?) indicating the status of the drive in question.

# Future potential functionality:
*Generate a simple GUI for visualization of the copy-over, delete, and various errors.
*The script will keep a list of copied files from drives and enable the user to select and move the files into a folder of a chosen name.
*The script will use small pointer files locally stored on the drive [that are ignored during copy/delete] to identify the source of the drive (such as photos, a certain camera, etc.) and place the files into sub-folders bearing the corresponding ID. (Could this also be done using a hardware ID? [if unique])
