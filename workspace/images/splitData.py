import os.path
import sys
import shutil

imgFolderPath = sys.argv[1]

numberOfFiles = 1
for file in os.listdir(imgFolderPath):
	if file.endswith("jpg") or file.endswith("jpeg") or file.endswith("png"):
		if numberOfFiles <= 1000:
			shutil.move(file, "train/" + file)
		else:
			shutil.move(file, "test/" + file)

		numberOfFiles = numberOfFiles + 1
