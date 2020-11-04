#*****************************************************************#
'''
This module parses the input file and step by step converts the
information of gates, their inputs and their outputs into the native
python formats(i.e. python objects). Later this format will be
useful to convert it into a directed acyclic graph(DAG).
'''
#*****************************************************************#

from classes import Gate


# A helper of get_eq_gate() to package 'inputs' and 'output' attributes nicely
def get_inputs_output(string, start):
  inputs = []
  i = start
  while(string[i] != ')'):
    node = ""
    while(string[i + 1] != ')' and string[i + 1] != ','):
      i += 1
      if (string[i] != ' '):
        node = node + string[i]
    inputs.append(node)
    i += 1
  output = inputs.pop(0);
  return (inputs, output)

# Converts a line 'string' read from the file to a Gate object
def get_eq_gate(string, start):
  i = start;
  name = "";
  while(string[i] != '('):
    name = name + string[i];
    i += 1;
  (inputs, output) = get_inputs_output(string, i);
  return Gate(name, inputs, output) 

# A method to control the flow towards get_eq_gate() function
def str_to_gate(string):
  if (string[0:2] == "or"):
    return get_eq_gate(string, 3)
  elif (string[0:4] == "nand" or string[0:4] == "xnor"):
    return get_eq_gate(string, 5)
  elif (string[0:3] == "and" or string[0:3] == "not" or string[0:3] == "nor" or string[0:3] == "xor"):
    return get_eq_gate(string, 4)
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

# reads the line containing input/output symbols based upon the 'string'
def get_io(fp, string):
  content = fp.readlines()
  fp.seek(0)
  for line in content:
    if(line[0:5] == string):
      return line

# Returns the input nodes
def get_input_list(fp):
  input_line = get_io(fp, "input")
  input_list = []
  i = 5
  while(input_line[i] != ';'):
    node = ""
    while(input_line[i + 1] != ';' and input_line[i + 1] != ','):
      i += 1
      if (input_line[i] != " "):
        node = node + input_line[i]
    input_list.append(node)
    i += 1
  return input_list

# Returns the output nodes
def get_output_list(fp):
  output_line = get_io(fp, "outpu")
  output_list = []
  i = 5
  while(output_line[i] != ';'):
    node = ""
    while(output_line[i + 1] != ';' and output_line[i + 1] != ','):
      i += 1
      if (output_line[i] != " "):
        node = node + output_line[i]
    output_list.append(node)
    i += 1
  return output_list

#*****************************************************************#
