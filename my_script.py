#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import numpy as np
import osmnx as ox
import networkx as nx
import json
import os
import pandas as pd
from prerun import Manhattan_Graph

# origin = sys.argv[1].strip().split(",")
# dest = sys.argv[2].strip().split(",")

# Manhattan_Graph = ox.graph_from_place('Manhattan Island, New York City, New York, USA', network_type='drive')
# point = (float(y[1]), float(y[0]))
# nearest_node_id = ox.get_nearest_node(Manhattan_Graph, point)
# lat = Manhattan_Graph.node[nearest_node_id]['y']
# lng = Manhattan_Graph.node[nearest_node_id]['x']
# data = {'id': nearest_node_id, 'latitude': lat, 'longitude': lng}
# # To write to a file:
# with open("/Users/shuogong/VisionZeroWebApp/output.json", "w") as f:
#     json.dump(data, f)
# print(str(data))

# point = (float(sys.argv[2]), float(sys.argv[1]))
# print(float(origin[1]), float(origin[0]), float(dest[1]), float(dest[0]))

# To print out the JSON string (which you could then hardcode into the JS)
# json.dumps(data)

# print('' + lat+','+lng)
# print('nearest node latlng is '+ '(' + lat + ',' + lng + ')')


def penalized_graph(Graph,collision_count,alpha):
    Modified_Graph = Graph.copy()
    for start_node,end_node, edge_data in Modified_Graph.edges(data=True):
            if (start_node in list(collision_count['nodeID'])):
                collisions = collision_count[collision_count['nodeID']==start_node]['count'].iloc[0]
                edge_data['length']= edge_data['length'] + alpha * collisions
    return Modified_Graph

def path_and_distance(Graph, origin_node, destination_node):
    route = nx.shortest_path(Graph, origin_node, destination_node, weight='length')
    distance = nx.shortest_path_length(Graph, origin_node, destination_node, weight='length')
    return route,distance

origin = sys.argv[1].strip().split(",")
dest = sys.argv[2].strip().split(",")

# Manhattan_Graph = ox.graph_from_place('Manhattan Island, New York City, New York, USA', network_type='drive')

origin_point = (float(origin[1]), float(origin[0]))
origin_nearest_node_id = ox.get_nearest_node(Manhattan_Graph, origin_point)
# originlat = Manhattan_Graph.node[origin_nearest_node_id]['y']
# originlng = Manhattan_Graph.node[origin_nearest_node_id]['x']
dest_point = (float(dest[1]), float(dest[0]))
dest_nearest_node_id = ox.get_nearest_node(Manhattan_Graph, dest_point)
# destlat = Manhattan_Graph.node[dest_nearest_node_id]['y']
# destlng = Manhattan_Graph.node[dest_nearest_node_id]['x']
# data = {'origin id': origin_nearest_node_id, 'origin latitude': originlat, 'origin longitude': originlng, 'dest id': dest_nearest_node_id, 'dest latitude': destlat, 'dest longitude': destlng}
# # To write to a file:
# with open("output.json", "w") as f:
#     json.dump(data, f)
# print(str(data))
collision_count = pd.read_csv("NY_collision_count.csv")
modified_graph = penalized_graph(Manhattan_Graph,collision_count,1)
r,d = path_and_distance(modified_graph, origin_nearest_node_id,dest_nearest_node_id)

latlng_list = []
latlng_center = []
latitude_total = 0
longitude_total = 0
for i in r:
    temp_list = []
    temp_list.append(Manhattan_Graph.node[i]['x'])
    temp_list.append(Manhattan_Graph.node[i]['y'])
    latlng_list.append(temp_list)

for i in latlng_list:
    latitude_total = latitude_total + i[0]
    longitude_total = longitude_total + i[1]
avg_lat = latitude_total/len(latlng_list)
avg_lng = longitude_total/len(latlng_list)
latlng_center.append(avg_lat)
latlng_center.append(avg_lng)

data = {'path_coordinates': latlng_list, 'center': latlng_center}
# To write to a file:
with open("/Users/shuogong/VisionZeroWebApp/output.json", "w") as f:
    json.dump(data, f)

print(str(data))
