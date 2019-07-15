# -*- coding: utf-8 -*-
# Author:	Ruslan Pantaev
# Date:		2017-12-28
# reference: 	https://medium.freecodecamp.org/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe
# example site: http://www.midiworld.com/bach.htm

import re
import requests
import urllib2
from bs4 import BeautifulSoup
import os, errno

quote_page = 'http://www.midiworld.com/'

# enter composer name here:
# composers = ['bach', 'bartok', 'beethoven', 'brahms', 'byrd', 'chopin', 'haydn', 'handel', 'hummel', 'liszt', 'mendelssohn',
# 	'mozart', 'rachmaninov', 'scarlatti', 'schumann', 'scriabin', 'shostakovich', 'tchaikovsky', 'earlymus']

composers = ['bach']

for composer in composers:
	directory = 'midi/' + composer + '/'

	try:
	    os.makedirs(directory)
	except OSError as e:
	    if e.errno != errno.EEXIST:
	        raise

	page = urllib2.urlopen(quote_page + composer + '.htm')
	soup = BeautifulSoup(page, "html.parser")

	for i, link in enumerate(soup.findAll('a', attrs={'href': re.compile(".mid$")})):
	    print link.get('href')
	    rq = urllib2.Request(link.get('href'))
	    name = str(link.get('href')).split("/")
	    res = urllib2.urlopen(rq)
	    midi = open(directory + name[-1], 'wb')
	    midi.write(res.read())
	    midi.close()
