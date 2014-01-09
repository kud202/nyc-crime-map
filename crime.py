#!/usr/bin/env python3
import os
import json

import requests

KEY = 'AIzaSyDW3Wvk6xWLlLI6Bfu29DuDaseX-g18_mo'
DIRECTORY = 'all_results'

def table():
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



#r = table()


def head():
    fn = 'head.geojson'
    if not os.path.exists(fn):
        fp = open(fn, 'xb')
        r = table_features('YR,MOgeometry,TOT,X,Y', maxResults = 10)
        fp.write(r.content)
        fp.close()

def mkpath(pageToken):
    filename = pageToken if pageToken else '__emptyToken__'
    return os.path.join(DIRECTORY, filename)

def mkfp(pageToken, mode = 'xb'):
    return open(mkpath(pageToken), mode)

def page(pageToken = None):
    '''
    Args: A pageToken or None
    Returns: The next pageToken or None
    '''

    path = mkpath(pageToken)
    if os.path.exists(path):
        return json.load(open(path))
    else:
        r = table_features('YR,MO,geometry,TOT,X,Y', maxResults = 1000, pageToken = pageToken)
        fp = mkfp(pageToken, mode = 'xb')
        fp.write(r.content)
        fp.close()
        return json.loads(r.text)

def pages(startPageToken = None):
    os.makedirs(DIRECTORY, exist_ok = True)

    if startPageToken:
        pageToken = startPageToken
    else:
        results = page()
        for result in results.get('features', []):
            yield result
        pageToken = results.get('nextPageToken')

    while pageToken:
        results = page(pageToken)
        for result in results.get('features', []):
            yield result
        pageToken = results.get('nextPageToken')

def geojson():
    pass

if __name__ == '__main__':
    head()
    p = pages()
