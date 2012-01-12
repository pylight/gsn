#!/bin/bash
# @desc: simple bashscript to upload images quickly to the server
# @info: ssh-add should be done before running this script!
# @author: pylight for http://ganz-sicher.net/blog (source: https://github.com/pylight/gsn)

# TODO:	+ fix variable / path chaos		+ ask for img class/alt text input


################
# Variables
################
sshArgs="gsn"			       # arguments for ssh/scp command to connect to the remote machine
uploadPath="jekyll/images/blog"	       # relative image path on remote machine (e.g. for cd command)
jekyllDir="jekyll"		       # relative jekyll path on the remote machine
finalPath="jekyll/_site/images/blog"   # the path where images should be after (re)generating the blog with jekyll
blogUri="http://ganz-sicher.net/blog/images/blog"  # the uri to the image path

################
# Functions
################

# do some checks before uploading
function checkBefore() {
   for ARG in "$@"
   do
      # check if file looks like an image
      fType=${ARG#*.} 
      case "$fType" in 
	 gif);;
	 GIF);;
	 jpg);;
	 jpeg);;
	 JPG);;
	 JPEG);;
	 png);;
	 PNG);;

	 *)
	 echo "Error: File $ARG (ext: $fType) doesn't look like an valid image!"
	 exit;;
      esac

      # check if local file exists
      curDir=$(/bin/pwd)
      if [ ! -e $curDir/$ARG ]
      then
      	 echo "Error: Local file $curDir/$ARG doesn't exist!"
      	 exit
      fi

      # check if remote file exists
      if ssh $sshArgs 'ls "'$uploadPath/$ARG'" &>/dev/null' 
      then
	 echo "Error: Remote File $ARG exists already!"
	 exit
      fi
   done
   echo # newline
}

# check if files got uploaded
function checkAfter()
{
   echo # newline 
   for ARG in "$@"
   do
      # check if remote file exists
      if ssh $sshArgs 'ls "'$finalPath/$ARG'" &>/dev/null' 
      then
         echo "Upload OK --> $blogUri/$ARG"
      else
      	 echo "!! WARNING: $blogUri/$ARG not found !!"
      fi
   done
}

function printImgTags(){
   # show img urls
   echo #newline
   echo "Image paths should be as follows:"
   echo "================================="
   for ARG in "$@"
   do
      echo "<img src=\"{{site.url}}/images/blog/$ARG\" class=\"\" alt=\"\" />"
   done
   echo #newline
}

################
# Main Code
################

# check args
if [ $# -lt 1 ]
then
   echo "Please give me at least one img to upload. :>"
else
   # check files
   checkBefore $*

   # upload img
   scp $* $sshArgs:$uploadPath
   
   # regenerate blog to copy img to actual path
   ssh gsn "cd $jekyllDir ; jekyll"

   checkAfter $*

   printImgTags $* 

fi
