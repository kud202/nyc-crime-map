#!/usr/bin/env python3
import os
import json

from time import sleep
from random import betavariate

import requests

KEY = 'AIzaSyDW3Wvk6xWLlLI6Bfu29DuDaseX-g18_mo'
DIRECTORY = os.path.join('data', 'all_results')

def randomsleep():
    'Sleep between zero and 100 seconds.'
    sleep(10 * betavariate(0.7, 8))

def table():
    '''
    This would tell us the schema, among other things.
    https://developers.google.com/maps-engine/documentation/reference/v1/tables#resource
    '''

    raise NotImplementedError('This doesn\'t work.')

    url = 'https://www.googleapis.com/mapsengine/v1/tables/02378420399528461352-11853667273131550346/'
    params = {
        'key': KEY,
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:24.0) Gecko/20100101 Firefox/24.0',
        'Referer':  'http://maps.nyc.gov/crime/',
    }
    r = requests.get(url, headers = headers, params = params)
    return r

def table_features(select, where = None, maxResults = 1000, pageToken = None):
    url = 'https://www.googleapis.com/mapsengine/v1/tables/02378420399528461352-11853667273131550346/features/'

    params = {
        'key': KEY,
        'version': 'published',
        'maxResults': maxResults,
        'select': select,
    }
    if where:
        params['where'] = where
    if pageToken:
        params['pageToken'] = pageToken

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:24.0) Gecko/20100101 Firefox/24.0',
        'Referer':  'http://maps.nyc.gov/crime/',
    }

    r = requests.get(url, headers = headers, params = params)
    return r

def head():
    fn = 'head.geojson'
    if not os.path.exists(fn):
        fp = open(fn, 'xb')
        r = table_features('YR,MO,geometry,TOT,X,Y', maxResults = 10)
        fp.write(r.content)
        fp.close()

def mkpath(pageToken, crime_type):
    filename = pageToken if pageToken else '__%s__' % (crime_type if crime_type else 'all_CR')
    return os.path.join(DIRECTORY, filename)

def mkfp(pageToken, crime_type, mode = 'xb'):
    return open(mkpath(pageToken, crime_type), mode)

def page(pageToken = None, crime_type = None):
    '''
    Args: A pageToken or None
    Returns: The next pageToken or None
    '''

    path = mkpath(pageToken, crime_type)
    if os.path.exists(path):
        return json.load(open(path))
    else:
        r = table_features('YR,MO,geometry,X,Y,TOT', maxResults = 1000, pageToken = pageToken)
        fp = mkfp(pageToken, crime_type, mode = 'xb')
        fp.write(r.content)
        fp.close()
        return json.loads(r.text)

def features(startPageToken = None, crime_type = None):
    os.makedirs(DIRECTORY, exist_ok = True)

    if startPageToken:
        pageToken = startPageToken
    else:
        print('Loading data for the inial search, without pageToken')
        results = page(crime_type = crime_type)
        for result in results.get('features', []):
            yield result
        pageToken = results.get('nextPageToken')

    while pageToken:
        print('Loading data for pageToken', pageToken)
        results = page(pageToken = pageToken, crime_type = crime_type)
        for result in results.get('features', []):
            yield result
        pageToken = results.get('nextPageToken')
        randomsleep()

def geojson():
    return {
        'type': 'FeatureCollection',
        'features': list(features()),
    }

def main():
    for crime_type in [
        'GRAND LARCENY',
        'GRAND LARCENY OF MOTOR VEHICLE',
    ]:
        for f in features(crime_type = crime_type):
            pass
    return


    path = os.path.join('data','crime.geojson')
    if not os.path.exists(path):
        data = geojson()
        json.dump(data, open(path, 'x'))

if __name__ == '__main__':
    # head()
    main()
