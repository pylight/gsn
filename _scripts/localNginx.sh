#!/bin/bash

# make sure docker is running
sudo systemctl start docker

# clean old containers
if [ -n "$(docker ps | grep nginx)" ] ; then
	echo -n "Killing "
	docker kill nginx
	echo -n "Removing "
	docker rm nginx
fi

echo "Starting new nginx container..."
docker run --name=nginx -d -p 127.0.0.1:80:80 -v $(pwd):/usr/share/nginx/html/ -v /opt/docker/nginx/default.conf:/etc/nginx/conf.d/default.conf:ro library/nginx
echo "Nginx should now be up and running on 127.0.0.1:80"
