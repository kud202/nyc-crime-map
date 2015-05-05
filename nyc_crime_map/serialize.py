import json
import vlermv

vlermv.Vlermv(output_directory, serializer = json)

def head(table_id, select):
    path = 'head-%s.geojson' % table_id
    if not os.path.exists(path):
        fp = open(path, 'xb')
        r = table_features(table_id, select, maxResults = 10)
        fp.write(r.content)
        fp.close()

def to_geojson(features):
    path = os.path.join('data',table_id + '.geojson')
    data = {
        'type': 'FeatureCollection',
        'features': features,
    }
    with open(path, 'w') as fp:
        json.dump(data, fp)

def to_csv(table_id, select):
    path = os.path.join('data',table_id + '.csv')
    fieldnames = ['longitude', 'latitude'] + select.split(',')
    fieldnames.remove('geometry')
    with open(path, 'w') as fp:
        w = csv.DictWriter(fp, fieldnames = fieldnames)
        w.writeheader()
        for feature in features(table_id, select):
            row = {
                'longitude': feature['geometry']['coordinates'][0],
                'latitude': feature['geometry']['coordinates'][1],
            }
            row.update(feature['properties'])
            w.writerow(row)

