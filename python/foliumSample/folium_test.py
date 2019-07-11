#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 damian <damian@damian-laptop>
#
# Distributed under terms of the MIT license.

"""
Sample of using folium libbrary (maps-based visualization library)
"""

import folium
import pandas
df=pandas.read_csv("Volcanoes_USA.txt")
map=folium.Map(location=[df['LAT'].mean(),df['LON'].mean()],zoom_start=6,tiles='Mapbox bright')
def color(elev):
    minimum=int(min(df['ELEV']))
    step=int((max(df['ELEV'])-min(df['ELEV']))/3)
    if elev in range(minimum,minimum+step):
        col='green'
    elif elev in range(minimum+step,minimum+step*2):
        col='orange'
    else:
        col='red'
    return col
fg=folium.FeatureGroup(name="Volcano Locations")
for lat,lon,name,elev in zip(df['LAT'],df['LON'],df['NAME'],df['ELEV']):
    fg.add_child(folium.Marker(location=[lat,lon],popup=(folium.Popup(name)),icon=folium.Icon(color=color(elev),icon_color='green')))
map.add_child(fg)
map.add_child(folium.GeoJson(data=open('world_geojson_from_ogr.json'),
name="Population",
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] <= 10000000 else 'orange' if 10000000 < x['properties']['POP2005'] < 20000000 else 'red'}))
map.add_child(folium.LayerControl())
map.save(outfile='map.html')
