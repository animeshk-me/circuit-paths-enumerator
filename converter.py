from classes import Gate

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
  GateData = get_gates_data(fp);
  
  # Below is the format to access the data in GateData list
  print(GateData[2].inputs);
  
  fp.close()
  # print("Some nonsense\n")


# Entry point
if __name__ == "__main__":
  main()
 