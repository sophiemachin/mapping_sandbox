import folium
import pandas as pd


uk_geo = 'result.json'
uk_data_csv = f'UK_data.csv'
uk_data = pd.read_csv(uk_data_csv)

m = folium.Map(location=[54, -2], zoom_start=6)

folium.Choropleth(
    geo_data=uk_geo,
    name='choropleth',
    data=uk_data,
    columns=['objectid', 'Amount'],
    key_on='id',
    fill_color='YlGn',
    fill_opacity=0.7,
    line_opacity=0.5,
    legend_name='Unemployment Rate (%)',
).add_to(m)

folium.LayerControl().add_to(m)


m.save('folium_chloropleth.html')
