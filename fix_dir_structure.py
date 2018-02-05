import shutil
import os
 
# copy all the files in the subfolders to main folder
 
# The current working directory
dest_dir = os.getcwd()
walker = os.walk(dest_dir)
 
rem_dirs = walker.next()[1]
 
for data in walker:
	for files in data[2]:
		try:
			shutil.move(data[0] + os.sep + files, dest_dir)
		except shutil.Error:
			continue
 
# clearing the directories
for dirs in rem_dirs:
	shutil.rmtree(dest_dir + os.sep + dirs)
