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

def get_path_and_center(Graph, origin_node_id,dest_node_id):
    r,d = path_and_distance(Graph, origin_node_id,dest_node_id)
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
    return latlng_list, latlng_center


origin = sys.argv[1].strip().split(",")
dest = sys.argv[2].strip().split(",")
# Manhattan_Graph = ox.graph_from_place('Manhattan Island, New York City, New York, USA', network_type='drive')
origin_point = (float(origin[1]), float(origin[0]))
origin_nearest_node_id = ox.get_nearest_node(Manhattan_Graph, origin_point)
dest_point = (float(dest[1]), float(dest[0]))
dest_nearest_node_id = ox.get_nearest_node(Manhattan_Graph, dest_point)
collision_count = pd.read_csv("NY_collision_count.csv")
modified_graph = penalized_graph(Manhattan_Graph,collision_count,1)

safest_latlng_list, safest_latlng_center = get_path_and_center(modified_graph, origin_nearest_node_id,dest_nearest_node_id)
shortest_latlng_list, shortest_latlng_center = get_path_and_center(Manhattan_Graph, origin_nearest_node_id,dest_nearest_node_id)

data = {'safest_path_coordinates': safest_latlng_list, 'safest_center': safest_latlng_center, 'shortest_path_coordinates': shortest_latlng_list, 'shortest_center': shortest_latlng_center}
# To write to a file:
with open("/Users/shuogong/VisionZeroWebApp/output.json", "w") as f:
    json.dump(data, f)

print(str(data))
