#!/bin/bash
# simple script to upload images quickly to my server
# probably only useful for myself ;p

# todo: 
# - ssh-add if needed
# - after *succ* upload: ask for deletion and echo path of img
# - check if img exists already

uploadpath="jekyll/images/blog"
jekylldir="jekyll"

# check args
if [ $# -lt 1 ]
then
   echo "Please give me at least one img to upload. :>"
else
   # upload img
   scp $* gsn:$uploadpath
   
   # regenerate blog to copy img to actual path
   ssh gsn "cd $jekylldir ; jekyll"

   # show img urls
   echo "Image paths should be as follows:"
   echo "================================="
   for ARG in "$@"
   do
      echo "{{site.url}}/images/blog/"$ARG
   done
   echo #newline
fi
