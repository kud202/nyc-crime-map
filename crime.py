#!/usr/bin/env python3
import json

import requests

def query(select, where, maxResults = 1000):

    url = 'https://www.googleapis.com/mapsengine/v1/tables/02378420399528461352-11853667273131550346/features/'

    params = {
        'key': 'AIzaSyDW3Wvk6xWLlLI6Bfu29DuDaseX-g18_mo',
        'version': 'published',
        'maxResults': maxResults,
        'select': select,
        'where': where,
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:24.0) Gecko/20100101 Firefox/24.0',
        'Referer':  'http://maps.nyc.gov/crime/',
    }

    r = requests.get(url, headers = headers, params = params)
    return json.loads(r.text)

select = 'geometry,TOT,X,Y'
where = '''MO=10 AND YR=2013 AND ST_INTERSECTS(geometry,ST_GEOMFROMTEXT('POLYGON((-73.92023205757141 40.7721081261999,-73.94100308418274 40.7721081261999,-73.94100308418274 40.76678598068301,-73.92023205757141 40.76678598068301,-73.92023205757141 40.7721081261999))')) AND X<>0 AND Y<>0'''

r = (query(select, where))
