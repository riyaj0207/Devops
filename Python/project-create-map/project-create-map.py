from msilib.schema import Icon
from turtle import color
from typing import List
import folium
from folium.plugins import MarkerCluster
from folium.features import CustomIcon

map=folium.Map(location=[20,78],zoom_start=6,tiles="Stamen Terrain")
icon_image="ticket.JPG"
icon = CustomIcon(
    icon_image,
    icon_size=(75, 95),
    icon_anchor=(10, 30),
)

x=[[20,78],[20,79],[20,80]]

fg=folium.FeatureGroup(name="my Map")
print(folium.__version__)
for cordinates in x:
    #map.add_child(folium.Marker(location=cordinates,icon=folium.Icon(color="red",icon="fa-hamburger", prefix='fa'),popup=folium.Popup('Hello chacha ')))
    map.add_child(folium.CircleMarker(location=cordinates,radius=6, fill_opacity=0.7,popup=folium.Popup('Hello chacha ')))

#fg=add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-stg').read()))

map.save("map5.html")

