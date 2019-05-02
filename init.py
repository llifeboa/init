import os
import json
import sys

def main():
	#config
	config = ""

	#file
	file = sys.argv[1] if len(sys.argv) == 2 else "config.json"

	#open file
	try:
		with open(file, "r") as config_file:
			config = json.loads(config_file.read())
	except Exception:
		exit("File Error")
	#rm old files/dirs
	for item in config.keys():
		rm(item)
	#create new files/dirs
	start(config)

#start create
def start(root):
	for item in root.keys():
		if "." in item:
			createFile(item)
		else:
			createDir(item)
			cd(item)
			start(root[item])
			cd("..")

#rm
def rm(dir):
	os.system("rm -rf {}".format(dir))

#cd
def cd(dir):
	os.chdir(dir)

#create dir
def createDir(dir):
	os.system("mkdir {}".format(dir))

#create file
def createFile(file):
	os.system("touch {}".format(file))

if __name__ == "__main__":
	main()