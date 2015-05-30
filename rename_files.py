import os
def rename_files():
	#(1) get file names from a folder
	file_list = os.listdir("/Users/geng/Dropbox/Udacity/Full Stack Web Developer Nanodegree/Programing Foundation with Python/prank")
	print(file_list)
	os.chdir("/Users/geng/Dropbox/Udacity/Full Stack Web Developer Nanodegree/Programing Foundation with Python/prank")
	print(os.getcwd())
	#(2) for each file, rename filename
	for file_name in file_list:
		os.rename(file_name, file_name.translate(None,"0123456789"))
	print(os.listdir("/Users/geng/Dropbox/Udacity/Full Stack Web Developer Nanodegree/Programing Foundation with Python/prank"))

rename_files()