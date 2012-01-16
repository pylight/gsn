#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @name: publishPost.py
# @author: pylight (https://github.com/pylight/) 
#
# @description: Phython 3 Helper Script to publish a jekyll posts (update the post-date and push it your git repo)
#
# @usage: 		python publishPost.py 												# will publish newest post (based on modification date)
#							python publishPost.py	post_filename.markdown	# will do the same with the specified post



from datetime import datetime
from sys import exit, argv
import os, readline, subprocess


# some  variables
postsDir = "/srv/http/jekyll/_posts/"	# local directory path that contains your posts
defExtension = "markdown" # the default file extension for your posts
sshArgs = "gsn"	# the arguments for the ssh command
# default git commands
commitCmd = "git commit -am "
statusCmd = "git status"
pushCmd = "git push origin master"

def checkArgs():
	numArgs = len(argv)
	if numArgs == 1:
		return 0
	elif numArgs == 2:
		return argv[0]
	else:
		exit("Usage: python publishPost.py [optional_post_filename]")

def setFileType():
	global fileType
	fileType = rlinput("File Extension: ", defExtension);

def filterType(f):
	return f.endswith("." + fileType)
		
# input with default value
def rlinput(prompt, prefill=''):
   readline.set_startup_hook(lambda: readline.insert_text(prefill))
   try:
      return input(prompt)
   finally:
       readline.set_startup_hook()



def main():
	print("\n--- publishPost.py Script ---")

	os.chdir(postsDir)
	
	if checkArgs():
		try:
			path = os.path.split(argv[1])
			fileName = path[1]
			f = open(fileName, 'r')
		except:
			exit("Error - Could not open post: " + argv[1])
		print("Using post " + fileName)
	else:
		print("No post filename given")
		print("Searching for newest post...")
	
		# post type / file extension
		setFileType()
	
		# search newest post
		filelist = os.listdir(postsDir)
		filelist = filter(lambda x: not os.path.isdir(x), filelist)
		filelist = filter(filterType, filelist)

		# find newest post	
		try:
			fileName = max(filelist, key=lambda x: os.stat(x).st_mtime)
		except ValueError:
			exit("Error, no posts found with filetype " + fileType + " in " + postsDir)
		
		print("Newest ." + fileType + " post: " + fileName)

		# search for date line
		f = open(fileName, 'r')
	
	# print metadata and get line with date-info
	newlines = []
	dateLine = -1
	metaEndLine = -2
	i = 0
	
	print("\n=> Metadata: ")
	for line in f:
		i = i + 1

		if metaEndLine < 0:
			print("\t" + str(i) + "  " + line, end='')

		if line == "---\n":
			if metaEndLine == -2:	# metadata begins
				metaEndLine = -1
			elif metaEndLine == -1:
				metaEndLine = i			# metadata ends

		if "date: " in line and metaEndLine == -1:
				dateLine = i
		
		newlines.append(line)

	f.close()

	if dateLine > 0:
		print("\nDate information seems to be in line " + str(dateLine) + " (if this is *wrong*, press Ctrl+C to cancel!)")
	else:
		print("\nCoundn't find a Line with a date information! Please check your file manually.")
		exit(-1)	

	if metaEndLine > 20 or metaEndLine < 0:
		print("Something seems to be wrong with the metadata of your post, please check the file manually!")
		exit(-1)

	# Date
	confirm = input("Update postdate? [Y/n] ")
	if confirm not in ('n', 'no', 'N', 'No', 'NO'):
		curdate = datetime.now()
		postdate = rlinput("Set new postdate: ", curdate.strftime("%Y-%m-%d %H:%M"))
		newlines[dateLine - 1] = "date: " + str(postdate) + "\n"
	
		# rewrite the file		
		f = open(fileName, 'w')
		f.writelines(newlines)
		f.close()
		print("New postdate written to file.")

		# check if filedate must be changed 
		splitNewDate = postdate.split(" ", 1)
		newFileDate = splitNewDate[0]
		oldFileDate = fileName[:10]
		
		# get filename-tail (filename without date)
		splitOldName = fileName.split("-", 3)
		fileNameEnd = splitOldName[3]

		# build new filename
		newFileName = newFileDate + fileNameEnd

		# optional: rename file		
		if newFileDate != oldFileDate:
			print("The day of the post has changed (old: " + oldFileDate + ", new: " + newFileDate + ")")
			confirmRename = input("Rename the filename to " + newFileName + "? [Y/n] ")
			if confirmRename not in ('n', 'no', 'N', 'No', 'NO'):
				os.rename(fileName, newFileName)

  # git status
	print("\nGit status:")
	print("=======================")
	statusOut = subprocess.check_output(statusCmd, shell=True)
	print(str(statusOut, encoding='utf8'), end="")
	print("=======================")
      
	# git add
	print("\nCustomize the git add command (leave empty to skip):")
	addCmd = rlinput("", "git add " + fileName)
	if addCmd != "":
		subprocess.check_output(addCmd, shell=True)

	# git commit
	print("\nCustomize the git commit msg (leave empty to skip commit):")
	commitMsg = rlinput("", "A new Post! (" + fileName + ")")
	if commitMsg != "":
		subprocess.check_output(commitCmd + "\"" + commitMsg + "\"", shell=True)

	# git push
	confirmPush = input("\nGit push (origin/master) [Y/n] ")
	if confirmPush not in ('n', 'no', 'N', 'No', 'NO'):
		subprocess.check_output(pushCmd, shell=True)
		print("\nDone. :) Now log in to your remote machine and run 'git pull' and 'jekyll' there!\n")
		
	return 0


if __name__ == '__main__':
	main()

