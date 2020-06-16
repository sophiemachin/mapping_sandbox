"""This cleans data from

https://data.gov.uk/dataset/5c23bf46-3dea-40bf-8f81-0e6f9095c9f6/european-electoral-regions-december-2018-boundaries-uk-bgc

(BGC) Generalised (20m)

"""

import json
uk_geo = 'European_Electoral_Regions__December_2018__Boundaries_UK_BGC.geojson'


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
                'name': d['properties']['eer18nm']
            },
            'geometry' : d['geometry']
        }
        cleaned['features'].append(feature)


with open('result.json', 'w') as fp:
    json.dump(cleaned, fp)

