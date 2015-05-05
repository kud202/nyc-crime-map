#!/usr/bin/env python3
import csv
import os
import json
import logging

from string import ascii_uppercase
import itertools

import vlermv
import requests

logger = logging.getLogger

KEY = 'AIzaSyDW3Wvk6xWLlLI6Bfu29DuDaseX-g18_mo'

@vlermv.cache('~/.vlermv', key_transformer = vlermv.transformers.archive())
def table_features(table_id, select, where = None, maxResults = 1000, pageToken = None):
    url = 'https://www.googleapis.com/mapsengine/v1/tables/%s/features/' % table_id

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
        'User-Agent': 'http://thomaslevine.com/!/nyc-crime-map',
        'Referer':  'http://maps.nyc.gov/crime/',
    }
    return requests.get(url, headers = headers, params = params)

def features(table_id, select, startPageToken = None):
    if startPageToken:
        pageToken = startPageToken
    else:
        logger.info('Loading data for the initial search, without pageToken')
        results = page(table_id, select)
        for result in results.get('features', []):
            yield result
        pageToken = results.get('nextPageToken')

    while pageToken:
        logger.info('Loading data for pageToken', pageToken)
        results = page(table_id, select, pageToken = pageToken)
        for result in results.get('features', []):
            yield result
        pageToken = results.get('nextPageToken')
