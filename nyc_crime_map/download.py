#!/usr/bin/env python3
import logging

import vlermv
import requests

logger = logging.getLogger(__name__)

KEY = 'AIzaSyDW3Wvk6xWLlLI6Bfu29DuDaseX-g18_mo'

@vlermv.cache('~/.nyc-crime-map/page',
    key_transformer = vlermv.transformers.archive())
def page(table_id, select, pageToken = None):
    '''
    Args: A pageToken or None
    Returns: The next pageToken or None
    '''

    r = table_features(table_id, select, maxResults = 1000)


@vlermv.cache('~/.nyc-crime-map/table_features_tail',
    key_transformer = vlermv.transformers.archive())
def table_features_startpage(table_id, select, pageToken):
    return _table_features(table_id, select, pageToken)

@vlermv.cache('~/.nyc-crime-map/table_features_first',
    key_transformer = vlermv.transformers.archive())
def table_features_startpage(table_id, select):
    return _table_features(table_id, select, None)

def _table_features(table_id, select, pageToken, where = None, maxResults = 1000):
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
