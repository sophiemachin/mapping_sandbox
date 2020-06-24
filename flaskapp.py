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

app = Flask(__name__)


@app.route('/')
def index():
    start_coords = (54, -2)
    folium_map = folium.Map(location=start_coords, zoom_start=6)
    return folium_map._repr_html_()


if __name__ == '__main__':
    app.run(debug=True)
