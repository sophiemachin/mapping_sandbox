import folium
import pandas as pd


uk_geo = 'result.json'
gb_data_csv = f'GB_data.csv'
gb_data = pd.read_csv(gb_data_csv)

m = folium.Map(location=[54, -2], zoom_start=6)

folium.Choropleth(
    geo_data=uk_geo,
    name='choropleth',
    data=gb_data,
    columns=['objectid', 'Amount'],
    key_on='id',
    fill_color='YlGn',
    fill_opacity=0.7,
    line_opacity=0.5,
    legend_name='Unemployment Rate (%)',
).add_to(m)

folium.LayerControl().add_to(m)


m.save('folium_chloropleth.html')
