import os
from logging import getLogger

from .download import table_features_first, table_features_tail
from .serialize import geojson, csv

logger = getLogger(__name__)

def nyc_crime_map(table_id, select, startPageToken = None):
    if startPageToken:
        pageToken = startPageToken
    else:
        logger.info('Loading data for the initial search, without pageToken')
        results = table_features_first(table_id, select).json()
        yield from results.get('features', [])
        pageToken = results.get('nextPageToken')

    while pageToken:
        logger.info('Loading data for pageToken %s' % pageToken)
        results = table_features_tail(table_id, select, pageToken).json()
        yield from results.get('features', [])
        pageToken = results.get('nextPageToken')

def cli():
    for table_id, select in [
         ('02378420399528461352-17772055697785505571', 'YR,MO,geometry,X,Y,TOT,CR'),
         ('02378420399528461352-11853667273131550346', 'YR,MO,geometry,X,Y,TOT'),
    ]:
        data = nyc_crime_map(table_id, select)
        basename = os.path.join('data', table_id)
        for f in [geojson, csv]:
            with open('%s.%s' % (basename, f.__name__), 'w') as fp:
                f(select, data, fp)

cli()
