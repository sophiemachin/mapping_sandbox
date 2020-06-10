import folium


m = folium.Map(
    location=[52.172031, 0.142177],
    zoom_start=15
)


m.save('index.html')
