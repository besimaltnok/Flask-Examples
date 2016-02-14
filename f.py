#!/usr/bin/env python
# -*- coding : utf-8 -*-

import os
import sys


static = ['css', 'js', 'img']

try:
	proje = sys.argv[1]
	if proje:
		for i in static:
			os.makedirs(proje+"/static/"+i)
		os.mkdir(proje+"/template")
		os.system("touch "+ proje+"/"+proje+'.py')

except IndexError:
		print "For use : ./f.py proje_name"
