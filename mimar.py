#!/usr/bin/env python
# -*- coding : utf-8 -*-
import os
import sys

"""
 # Flask Proje Yapısı #
Flask uygulamaları genellikle bu  yapı kullanılarak inşa edilir.
"""

static = ['css', 'js', 'img']

try:
	proje = sys.argv[1]
	if proje:
		for i in static:
			os.makedirs(proje+"/static/"+i)
		os.mkdir(proje+"/template")
		os.system("touch "+ proje+"/"+proje+'.py')
		print "\nProje Dosyalariniz Olusturulmustur\nBasarilar :)"
		os.system("cd "+proje+"&& "+"tree")
except IndexError:
		print "Kullanmak icin  :: ./mimar.py proje_ismi"
