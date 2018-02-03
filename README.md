# Midi_Webscraper

**Description**
* Beautiful Soup is beautiful.  For purposes of using Tensor Flow / Magenta for
generating ai music, data sets are crititcal.  Avoid the hassle of manually
downloading files and use this scraper.

-*- coding: utf-8 -*-  
Author:	Ruslan Pantaev  
Date:		2017-12-28  
reference: 	https://medium.freecodecamp.org/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe  
example site: http://www.midiworld.com/bach.htm  

**TODO**
* *Parse midi files with an algorithm to figure out the tonality / key of the piece
to catalog data sets accordingly.  Training with music in many tonalities produces
undesirable results*

* *Algorithim can either inspect file for most recurrent notes to determine key OR
use another webscraper to search the web for metadata (possibly less deterministic)*
