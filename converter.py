from classes import Gate, Graph

# Returns the graph equivalent of the data extracted from verilog file
def get_final_graph(gateData, input_list, output_list):
  graph = Graph();
  # make edges from input nodes
  for gate in gateData:
    for node in input_list:
      if(node in gate.inputs):
        graph.add_edge(node, gate.name)
  # make edges to output nodes
  for gate in gateData:
    for node in output_list:
      if(node == gate.output):
        graph.add_edge(gate.name, node)
  # make edges among internal nodes(gates)
  for src in gateData:
    for dest in gateData:
      if(src.output in dest.inputs):
        graph.add_edge(src.name, dest.name)
  return graph

# A helper of get_eq_gate() to package 'inputs' and 'output' attributes nicely
def get_inputs_output(str, start):
  inputs = []
  i = start + 1
  while(i < len(str) - 2):
    node = ""
    while(i < len(str) - 3 and str[i] != ','):
      node = node + str[i]
      i += 1
    inputs.append(node);
    i += 1
  output = inputs.pop(0);
  return (inputs, output)

# Converts a line 'str' read from the file to a Gate object
def get_eq_gate(str, start):
  i = start;
  name = "";
  while(str[i] != '('):
    name = name + str[i];
    i += 1;
  (inputs, output) = get_inputs_output(str, i);
  return Gate(name, inputs, output) 

# A method to control the flow towards get_eq_gate() function
def str_to_gate(str):
  if (str[0:2] == "or"):
    return get_eq_gate(str, 3)
  elif (str[0:4] == "nand" or str[0:4] == "xnor"):
    return get_eq_gate(str, 5)
  elif (str[0:3] == "and" or str[0:3] == "not" or str[0:3] == "nor" or str[0:3] == "xor"):
    return get_eq_gate(str, 4)
  else:
    return -1;

# Returns a list of Gate objects
def get_gates_data(fp):
  content = fp.readlines()
  fp.seek(0);
  gates_list = []
  for line in content:
    if(line[0:9] == "endmodule"):
      break;
    gate_data = str_to_gate(line);
    if(gate_data != -1):
      gates_list.append(gate_data)
  return gates_list

# reads the input/output symbols based upon the 'str'
def get_io(fp, str):
  content = fp.readlines()
  fp.seek(0);
  for line in content:
    if(line[0:5] == str):
      return line

# Returns the input nodes
def get_input_list(fp):
  input_line = get_io(fp, "input")
  input_list = []
  i = 6
  while(i < len(input_line) - 1):
    node = ""
    while(i < len(input_line) - 1 and input_line[i] != ',' and input_line[i] != ';'):
      node = node + input_line[i]
      i += 1
    input_list.append(node);
    i += 1
  return input_list


# Returns the output nodes
def get_output_list(fp):
  output_line = get_io(fp, "outpu")
  output_list = []
  i = 7
  while(i < len(output_line) - 1):
    node = ""
    while(i < len(output_line) - 1 and output_line[i] != ',' and output_line[i] != ';'):
      node = node + output_line[i]
      i += 1
    output_list.append(node);
    i += 1
  return output_list

# Main function
def main():
  fp = open("input.v", "r")
  input_list = get_input_list(fp)
  output_list = get_output_list(fp)
  print("Overall inputs", input_list)
  print("Overall outputs", output_list)
  gateData = get_gates_data(fp);
  
  #************************* For TK starts *************************#
  # Below is the format to access the data in gateData list
  print(gateData[2].inputs);
  
  # Declaring Graph
  G = Graph();
  v1 = "sanu"
  v2 = "good"
  v3 = "bad"
  v4 = "shit"

  # Adding edges
  G.add_edge(v1, v2)
  G.add_edge(v1, v3)
  G.add_edge(v3, v4)
  G.add_edge(v4, v2)
  G.add_edge(v2, v3)
  
  G.print_graph("example");
  #************************* For TK ends ***************************#
 
  final_graph = get_final_graph(gateData, input_list, output_list)  
  final_graph.print_graph("Final")

  fp.close()

# Entry point
if __name__ == "__main__":
  main()
 