#!/bin/bash
docker stop $(docker ps -a | grep flask-deploy | cut -d ' ' -f 1)
docker rm $(docker ps -a | grep flask-deploy | cut -d ' ' -f 1)
docker rmi --force $(docker images | grep flask-deploy | tr -s ' ' | cut -d ' ' -f 3 | uniq)
