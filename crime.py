#!/usr/bin/env python3
import os
import json

import requests

KEY = 'AIzaSyDW3Wvk6xWLlLI6Bfu29DuDaseX-g18_mo'

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

def table_features(select, where = None, maxResults = 1000):
    url = 'https://www.googleapis.com/mapsengine/v1/tables/02378420399528461352-11853667273131550346/features/'

    params = {
        'key': KEY,
        'version': 'published',
        'maxResults': maxResults,
        'select': select,
    }
    if where:
        params['where'] = where

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
        r = table_features('MO,YR,geometry,TOT,X,Y', maxResults = 10)
        fp.write(r.content)
        fp.close()

def all_results():
    pass


if __name__ == '__main__':
    head()
