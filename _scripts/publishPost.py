#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  publishPost.py
#  
#  Phython 3 Helper Script to publish a jekyll posts

# @usage: 		python pypublishPost.py 	# will publish newest post (based on modification date)

	# TODO	
	# - also rename post-file if the postday has changed
	# - ssh to remote - pull + regenerate blog		
	# - use filename as argument instead of newest post

from datetime import datetime
from sys import exit
import os, readline, subprocess


# some  variables
postsDir = "/srv/http/jekyll/_posts/"	# local directory path that contains your posts
defExtension = "markdown" # the default file extension for your posts

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

# generate the new file
def generatePost(title, date, category = ''):
	if category == '':
		post = 	"---\nlayout: post\ntitle: " + str(title) + "\ndate: " + str(date) + "\n---\n"
	else:
		post = 	"---\nlayout: post\ntitle: " + str(title) + "\ndate: " + str(date) + "\ncategory: " + str(category) + "\n---\n"
	return post

def main():
	print("\n--- publishPost.py Script ---")
		
	# post type / file extension
	setFileType()
	
	# search newest post
	os.chdir(postsDir)
	filelist = os.listdir(postsDir)
	filelist = filter(lambda x: not os.path.isdir(x), filelist)
	filelist = filter(filterType, filelist)

	# find newest post	
	try:
		fileName = max(filelist, key=lambda x: os.stat(x).st_mtime)
	except ValueError:
		print("Error, no posts found with filetype " + fileType + " in " + postsDir)
		return -1	
		
	print("Newest ." + fileType + " post: " + fileName)

	# search for date line
	f = open(fileName, 'r')
	
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
	confirm = input("Update Postdate? [Y/n] ")
	if confirm not in ('n', 'no', 'N', 'No', 'NO'):
		curdate = datetime.now()
		postdate = rlinput("Set new postdate: ", curdate.strftime("%Y-%m-%d %H:%M"))
		newlines[dateLine - 1] = "date: " + str(postdate) + "\n"
		
		# rewrite the file		
		f = open(fileName, 'w')
		f.writelines(newlines)
		f.close()
		print("New PostDate written to File.")

	# git add
	addCmd = "git add " + fileName
	subprocess.check_output(addCmd, shell=True)

	# git commit
	print("\nCustomise the git commit msg:")
	commitCmd = "git commit -am "
	commitMsg = rlinput("", "A new Post! (" + fileName + ")")
	subprocess.check_output(commitCmd + "\"" + commitMsg + "\"", shell=True)

	# git push
	pushCmd = "git push origin master"
	subprocess.check_output(pushCmd, shell=True)
	
	print("Done. :) Now log in to your remote maschine and run 'git pull' and 'jekyll' there.")
		
	
	return 0

if __name__ == '__main__':
	main()

