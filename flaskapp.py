""" flask_example.py

    Required packages:
    - flask
    - folium

    Usage:

    Start the flask server by running:

        $ python flask_example.py

    And then head to http://127.0.0.1:5000/ in your browser to see the map displayed

"""

from flask import Flask

import folium
import pandas as pd
app = Flask(__name__)


@app.route('/')
def index():

    uk_geo = 'result.json'
    uk_data_csv = f'UK_data.csv'
    uk_data = pd.read_csv(uk_data_csv)

    m = folium.Map(
        location=[54.5, -2],
        zoom_start=6,
        tiles='Mapbox Bright',
    )

    folium.Choropleth(
        geo_data=uk_geo,
        name='choropleth',
        data=uk_data,
        columns=['objectid', 'Amount'],
        key_on='id',
        fill_color='YlGn',
        fill_opacity=0.7,
        line_opacity=0.5,
        legend_name='Accent',
    ).add_to(m)
    
    return m._repr_html_()


if __name__ == '__main__':
    app.run(debug=True)
