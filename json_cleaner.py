"""This cleans data from

https://data.gov.uk/dataset/3b2fde41-decf-4d5e-8642-95dd8127ac23/european-electoral-regions-december-2016-generalised-clipped-boundaries-in-great-britain

"""

import json
uk_geo = 'European_Electoral_Regions__December_2016__Boundaries.geojson'


cleaned = {
    "type": "FeatureCollection",
    "features": [],
}

with open(uk_geo) as json_file:
    data = json.load(json_file)
    for d in data['features']:
        print(d)
        feature = {
            "type": "Feature",
            "id": d['properties']['objectid'],
            "properties": {
                'name': d['properties']['eer16nm']
            },
            'geometry' : d['geometry']
        }
        cleaned['features'].append(feature)


with open('result.json', 'w') as fp:
    json.dump(cleaned, fp)

