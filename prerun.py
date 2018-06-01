# prerun.py

import osmnx as ox
import networkx as nx
import seaborn as sns
sns.set()
ox.config(log_file=False, log_console=False, use_cache=True)

Manhattan_Graph = ox.graph_from_place('Manhattan Island, New York City, New York, USA', network_type='drive')
