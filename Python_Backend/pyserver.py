# API code for Vision Zero
# Richard Sowers <r-sowers@illinois.edu>
# Copyright 2018 University of Illinois Board of Trustees. All Rights Reserved. Licensed under the MIT license
#
# use: python pyserver.py
#
# localhost:8081?origin=4163883691&destination=42435675&alpha=0.123
# localhost:8081?origin=42435310&destination=42440710&alpha=0.123

from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, urlsplit, parse_qs
import sys
import json
import osmnx
import networkx
import pandas
import numpy
import time
import itertools
import pickle
import importlib
import multiprocessing
import sys
import FINAL_config_hour_of_day as config






# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):

  # GET

  def do_GET(self):
    try:
      print("path: "+str(self.path))
      query=urlsplit(self.path).query
      print("query: "+str(query))
      params=parse_qs(query)
      print("params: "+str(params))
      origin = params["origin"][0].strip().split(",")
      dest = params["destination"][0].strip().split(",")
      origin_point = (float(origin[1]), float(origin[0]))
      origin = osmnx.get_nearest_node(G_raw, origin_point)
      dest_point = (float(dest[1]), float(dest[0]))
      destination = osmnx.get_nearest_node(G_raw, dest_point)
      alpha=float(params["alpha"][0])

      networkx.set_edge_attributes(G,numpy.inf,"cost")
      for edge in G.edges:
        #print(begin,end)
        G.edges[edge]["cost"]=(1-alpha)*G.edges[edge]["time"]+alpha*G.edges[edge]["accidents"]

      cheapest_path=networkx.shortest_path(G, source=origin,target=destination, weight="cost")
      quickest_path=networkx.shortest_path(G, source=origin,target=destination, weight="time")

      get_path_and_center(G, origin,destination,alpha,"cost")

      print("cheapest path: "+str(cheapest_path))
      print("quickest path: "+str(quickest_path))

      #query = urlsplit(url).query
     #params = parse_qs(query)
      #print("parsed path: "+str(urldata))

      # Send response status code
      self.send_response(200)

      outData={}
      outData["origin"]=origin
      outData["destination"]=destination
      outData["quickest_path"]=cheapest_path
      outData["cheapest_path"]=quickest_path
      print("outData: "+str(outData))


      # Send headers
      self.send_header('Content-type','text/html')
      self.end_headers()

      # Send message back to client
      message = json.dumps(outData)
      print("message: "+str(message))
      #self.wfile.write("<html><body><h1>hi!</h1></body></html>")
      # Write content as utf-8 data
      self.wfile.write(bytes(message, "utf8"))

    except Exception as e:
      print("exception: "+str(e))
      #sys.exit()

def run():
  print('starting server...')

  # Server settings
  # Choose port 8080, for port 80, which is normally used for a http server, you need root access
  server_address = ('127.0.0.1', 8081)
  httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
  print('running server...')
  httpd.serve_forever()

def get_path_and_center(Graph, origin_node_id,dest_node_id,alpha,weight):
  r = networkx.shortest_path(Graph, origin_node_id,dest_node_id, weight)
  latlng_list = []
  latlng_center = []
  latitude_total = 0
  longitude_total = 0
  for i in r:
      temp_list = []
      temp_list.append(G_raw.node[i]['x'])
      temp_list.append(G_raw.node[i]['y'])
      latlng_list.append(temp_list)
  for i in latlng_list:
      latitude_total = latitude_total + i[0]
      longitude_total = longitude_total + i[1]
  avg_lat = latitude_total/len(latlng_list)
  avg_lng = longitude_total/len(latlng_list)
  latlng_center.append(avg_lat)
  latlng_center.append(avg_lng)
  data = {'coordinates': latlng_list, 'center': latlng_center, 'alpha': alpha}
  # To write to a file:
  with open("/Users/shuogong/VisionZeroWebApp/output.json", "w") as f:
      json.dump(data, f)

if __name__ == '__main__':
  global G
  windower=config.windower() #config should default to entire dataset
  osmnx.config(log_file=True, log_console=True, use_cache=True)
  G_raw = osmnx.graph_from_place('Manhattan Island, New York, USA', network_type='drive')
  G=networkx.DiGraph(G_raw.copy())

  print("INITIALIZING ACCIDENT DATA")
  accidents_raw=config.accidents(windower.timewindower)
  accidents=accidents_raw.copy()
  accidents.set_index("node",drop=True,inplace=True)
  accidents=accidents.groupby(level="node").size()
  networkx.set_edge_attributes(G,0,"accidents")
  #set default value of zero accidents
  for node,count in accidents.iteritems():
    try:
      for edge in G.in_edges(node):
        G.edges[edge]["accidents"]=count
    except Exception: #fails if node is not in graph
      pass


  print("INITIALIZING TRAVELTIME DATA")
  traveltimes_raw=config.traveltimes(windower.timewindower)
  traveltimes=traveltimes_raw.copy()
  traveltimes.set_index(["begin_node","end_node"],drop=True,inplace=True)
  traveltimes_means=traveltimes["travel_time"].groupby(level=["begin_node","end_node"]).mean()
  #set default value of infinite time.
  networkx.set_edge_attributes(G,numpy.inf,"time")
  for edge,traveltime in traveltimes_means.iteritems():
    try:
      G.edges[edge]["time"]=traveltime
    except Exception: #fails if (begin,end) is not in graph
      pass
  print('starting server...')

  # Server settings
  # Choose port 8080, for port 80, which is normally used for a http server, you need root access
  server_address = ('127.0.0.1', 8081)
  httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
  print('running server...')
  httpd.serve_forever()
