#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  newpost.py
#  
#  Phython 3 Helper Script to make a new post in jekyll
#  
#  ToDos:
#  - category select
#  - start with parameters
#  - other types (page, drafts)

from datetime import datetime
import readline
import re
from subprocess import Popen

# globals
version = "0.1"
useCategories = True
defaultEditor = "geany"
postsDir = "/srv/http/jekyll/_posts/"
fileType = "markdown"

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

def prepareFilename(date, title):
	# Remove all non-word characters (everything except numbers and letters)
	title = re.sub(r"\W", ' ', title)
	
	# Replace all runs of whitespace with a single dash
	title = re.sub(r"\s+", '-', title)

	# replace umlauts
	title = title.replace("ä", "a")
	title = title.replace("ö", "o")
	title = title.replace("ü", "u")
	title = title.replace("ß", "s")

	# remove last char if it is a '-'
	if title[-1] == '-':
		title = title[:-1]
	
	filename = date + "-" + title	
	return filename



def main():
	print(" --- newpost.py v" + version + " --- ")
	
	# Title
	title = input("NewPost Title: ")
	
	# Date
	curdate = datetime.now()
	postdate = rlinput("NewPost Date: ", curdate.strftime("%Y-%m-%d"))
	
	# Category
	if useCategories:
		category = input("NewPost Category: ")
	else:
		category = ""
	
	postContent = generatePost(title, postdate, category)

	# create the file
	filename = prepareFilename(postdate, title)

	path = postsDir + filename + "." + fileType
	print("creating " + path)
	postFile = open(path, "w")
	postFile.writelines(postContent)

	# choose editor & open
	editor = rlinput("Editor: ", defaultEditor)
	openCmd = editor + " " + path
	Popen(openCmd, shell=True)
	
	return 0

if __name__ == '__main__':
	main()

