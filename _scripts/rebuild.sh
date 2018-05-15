#!/bin/bash
BLOG_PATH="/var/www/blog/"
JEKYLL_PATH="/home/me-server/jekyll/"
TIMESTAMP=$(date +%s)
BACKUP_PATH="/tmp/blog-$TIMESTAMP/"

if [[ $EUID -ne 0 ]]; then
  echo "Please run as root!" 2>&1
  exit 1
fi

cd $JEKYLL_PATH
jekyll build && mv $BLOG_PATH $BACKUP_PATH && mv $JEKYLL_PATH/_site/ $BLOG_PATH
echo "Rebuilding successful :)"
exit 0
