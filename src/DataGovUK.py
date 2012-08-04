'''
Created on Jul 11, 2012

@author: petrbouchal
'''

#===============================================================================
# Objective: find all data packages on data.gov.uk matching a certain query, populate index, and build database with data [to be specified]
#===============================================================================

testrun = 1

import json
import urllib2
import urllib
from pprint import pprint

# set base url for API
baseurl = 'http://data.gov.uk/api/2/'

# set what part of API is being used
functionbit = 'search/package'

# perform search and pickup 
url = baseurl + functionbit
# TODO: make this general so that API search terms can be picked up from a database/list
searchquery = '"workforce management information"'
params = urllib.urlencode({'q': searchquery, 'limit': 100})
try:
    searchresult0 = urllib2.urlopen(url, params)
except IOError:
    print('API unavailable on initial search call.')
#    raise
    quit
searchresult = searchresult0.read()
searchresultsJ = json.loads(searchresult)
#pprint(searchresultsJ)

#print srchresultsJ['results'][0]

# retrieve package details
functionbit = 'rest/package/'

for package in searchresultsJ['results']:
    url = baseurl + functionbit + searchresultsJ['results'][package]
    dataset = urllib2.urlopen(url)
    data = dataset.read()
    jsondataset = json.loads(data)
    pprint(jsondataset)
    for release in jsondataset['data']:
        break #TODO: build routine to pick up data pieces from API 

