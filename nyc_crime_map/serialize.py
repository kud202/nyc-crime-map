import json
import vlermv

vlermv.Vlermv(output_directory, serializer = json)

def to_geojson(obj, fp):
    data = {
        'type': 'FeatureCollection',
        'features': obj,
    }
    json.dump(data, fp)

def to_csv(select, obj, fp):
    fieldnames = ['longitude', 'latitude'] + select.split(',')
    fieldnames.remove('geometry')

    w = csv.DictWriter(fp, fieldnames = fieldnames)
    w.writeheader()
    for feature in obj:
        row = {
            'longitude': feature['geometry']['coordinates'][0],
            'latitude': feature['geometry']['coordinates'][1],
        }
        row.update(feature['properties'])
        w.writerow(row)
