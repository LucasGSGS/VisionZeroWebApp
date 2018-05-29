#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import numpy as np
import osmnx as ox
import json
import os


Manhattan_Graph = ox.graph_from_place('Manhattan Island, New York City, New York, USA', network_type='drive')
point = (float(sys.argv[2]), float(sys.argv[1]))
nearest_node_id = ox.get_nearest_node(Manhattan_Graph, point)
lat = Manhattan_Graph.node[nearest_node_id]['y']
lng = Manhattan_Graph.node[nearest_node_id]['x']
data = {'latitude': lat, 'longitude': lng}
# To write to a file:
with open("/Users/shuogong/VisionZeroWebApp/output.json", "w") as f:
    json.dump(data, f)
print(str(data))

# point = (float(sys.argv[2]), float(sys.argv[1]))
# print(str(point))

# To print out the JSON string (which you could then hardcode into the JS)
# json.dumps(data)

# print('' + lat+','+lng)
# print('nearest node latlng is '+ '(' + lat + ',' + lng + ')')