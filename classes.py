from collections import defaultdict

class Gate:
  
  def __init__(self, name, inputs, output):
    self.name = name
    self.inputs = inputs
    self.output = output




class Graph:
  def __init__(self):
    self.adj = defaultdict(list)
  
  # Adds a directed edge from a to b (a---->b)
  def add_edge(self, a, b):
    self.adj[a].append(b)

  # prints the graph
  def print_graph(self, name):
    print(f"The graph {name}:\n_________________________________")
    for vertex in self.adj:
      print(vertex, "--->", self.adj[vertex])
    print("_________________________________\n");


# class Node:
#   def __init__(self, name):
