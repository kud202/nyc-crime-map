#!/usr/bin/enw python3
import json

import requests


url = 'https://www.googleapis.com/mapsengine/v1/tables/02378420399528461352-11853667273131550346/features/?key=AIzaSyDW3Wvk6xWLlLI6Bfu29DuDaseX-g18_mo&version=published&maxResults=1000&select=geometry,TOT,X,Y&where=MO%3D10%20AND%20YR%3D2013%20AND%20ST_INTERSECTS(geometry%2CST_GEOMFROMTEXT(%27POLYGON((-73.92023205757141%2040.7721081261999%2C-73.94100308418274%2040.7721081261999%2C-73.94100308418274%2040.76678598068301%2C-73.92023205757141%2040.76678598068301%2C-73.92023205757141%2040.7721081261999))%27))%20AND%20X%3C%3E0%20AND%20Y%3C%3E0'

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:24.0) Gecko/20100101 Firefox/24.0',
    'Referer':  'http://maps.nyc.gov/crime/',
}

r = requests.get(url, headers = headers)
print(json.loads(r.text))
