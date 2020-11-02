from collections import defaultdict

#***************************************************************#

# A Gate class to package all the data of a gate
class Gate:
  def __init__(self, name, inputs, output):
    self.name = name
    self.inputs = inputs  # list of inputs
    self.output = output  # only one output(primitive gates)

#***************************************************************#

# A Graph class to represent a graph using adjancency list
class Graph:
  def __init__(self):
    self.adj = defaultdict(list) # Adjacency list
  
  # Adds a directed edge from a to b (a---->b)
  def add_edge(self, a, b):
    self.adj[a].append(b)

  # prints the graph
  def print_graph(self, name):
    print(f"The graph {name}:\n----------------------------")
    for vertex in self.adj:
      print(vertex, "--->", self.adj[vertex])
    print("-----------------------------------\n");

#***************************************************************#
