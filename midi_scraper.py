# -*- coding: utf-8 -*-
# Author:		Ruslan Pantaev
# Date:			2017-12-28
# reference: 	https://medium.freecodecamp.org/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe
# example site: http://www.midiworld.com/bach.htm

import re
import requests
import urllib2
from bs4 import BeautifulSoup
import os, errno

# quote_page = 'http://www.midiworld.com/bach.htm'

# # query the website and return the html to the variable ‘page’
# page = urllib2.urlopen(quote_page)

# # parse the html using beautiful soup and store in variable `soup`
# soup = BeautifulSoup(page, "html.parser")

# # for x in soup.find_all('x', href=True):
# #     print "Found the URL:", a['href']

# # midi = soup.find_all(href=True)
# midi = soup.find_all(href=re.compile(".mid$"))

# for a in midi:
# 	filename = a.get('src')
# 	data = urllib2.urlopen(filename).read()
	



# with open( "myfile.midi", "wb" ) as code:
# 	code.write(data)

# # print soup.find('a', href = re.compile(r'.*follow\?page.*'))

# ------------------------------------------------------------------

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

	page = urllib2.urlopen('http://www.midiworld.com/' + composer + '.htm')
	soup = BeautifulSoup(page, "html.parser")

	for i, link in enumerate(soup.findAll('a', attrs={'href': re.compile(".mid$")})):
	    print link.get('href')
	    rq = urllib2.Request(link.get('href'))
	    name = str(link.get('href')).split("/")
	    res = urllib2.urlopen(rq)
	    midi = open(directory + name[-1], 'wb')
	    midi.write(res.read())
	    midi.close()