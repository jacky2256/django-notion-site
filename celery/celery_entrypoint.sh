#!/bin/bash
DATE_NOW=$(date +"%Y%m%d")
celery -A core worker -P threads -l info -E  -c 10 --loglevel=INFO --logfile=../code/logs/celery_"$DATE_NOW".log