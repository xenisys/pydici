#!/bin/sh
killall memcached 
/usr/sbin/memcached -l 127.0.0.1 -d 
python manage.py runserver 8888
killall memcached 
