#*****************************************************************#
'''
* This module is essentially used to transform the gates and their
  input/output information into a directed acyclic graph(DAG). 

* Other functions which exist in this module inherently use a graph
  algorithm called Breadth first search(BFS) to enumerate all paths
  from inputs to outputs in the overall circuit recursively.
'''
#*****************************************************************#

from classes import Graph

# Return a list of all possible paths from every input to every output
def get_final_paths(input_list, output_list, graph):
  all_paths = []
  for ip in input_list:
    for op in output_list:
      this_paths = get_all_paths(ip, op, graph)
      all_paths.extend(this_paths)
  return all_paths

# append the string a at the start of every paths in list u_paths
def append_a(a, u_paths):
  a_paths = [f"({a})--->{path}" for path in u_paths]
  return a_paths

# Return a list of all possible paths from node a to node b in the graph
def get_all_paths(a, b, graph):
  paths = []
  if(a == b):
    paths.append(f"({b})")
    return paths
  for u in graph.adj[a]:
    u_paths = get_all_paths(u, b, graph)
    a_paths = append_a(a, u_paths)  # append a at the beginning
    paths.extend(a_paths)        # append new paths to the paths from a to b
  return paths

# Return the graph equivalent of the gate_data extracted from verilog file
def get_final_graph(gate_data, input_list, output_list):
  graph = Graph();
  # make edges from input nodes
  for gate in gate_data:
    for node in input_list:
      if(node in gate.inputs):
        graph.add_edge(node, gate.name)
  # make edges to output nodes
  for gate in gate_data:
    for node in output_list:
      if(node == gate.output):
        graph.add_edge(gate.name, node)
  # make edges among internal nodes(gates)
  for src in gate_data:
    for dest in gate_data:
      if(src.output in dest.inputs):
        graph.add_edge(src.name, dest.name)
  return graph


#*****************************************************************#
