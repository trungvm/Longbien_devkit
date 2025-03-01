#!/bin/bash

docker commit $(docker ps -l -q) lifezero/junbot-base:latest



