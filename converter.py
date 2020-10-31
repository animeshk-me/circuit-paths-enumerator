from classes import Gate

def get_inputs_output(str, start):
  # input_line = get_io(fp, "input")
  inputs = []
  i = start + 1
  while(i < len(str) - 2):
    node = ""
    while(i < len(str) - 3 and str[i] != ','):
      node = node + str[i]
      i += 1
    # print("hi", node);
    inputs.append(node);
    i += 1
  output = inputs.pop(0);
  # print(inputs);
  return (inputs, output)
  # return input_list


def get_eq_gate(str, start):
  i = start;
  name = "";
  # print("hello")
  while(str[i] != '('):
    name = name + str[i];
    i += 1;
  (inputs, output) = get_inputs_output(str, i);
  print(Gate(name, inputs, output)) # use .output or .inputs or .name to print and verify the Gate object here. We will eventually return this object to caller function

# useless
def get_nand_xnor(str, start):
  pass
# useless
def get_remaining_gate(str, start):
  pass

def str_to_gate(str):
  if (str[0:2] == "or"):
    return get_eq_gate(str, 3)
  elif (str[0:4] == "nand" or str[0:4] == "xnor"):
    return get_eq_gate(str, 5)
  elif (str[0:3] == "and" or str[0:3] == "not" or str[0:3] == "nor" or str[0:3] == "xor"):
    return get_eq_gate(str, 4)
  else:
    return -1;

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


def main():
  fp = open("input.v", "r")
  input_list = get_input_list(fp)
  output_list = get_output_list(fp)
  print(input_list)
  print(output_list)
  GateData = get_gates_data(fp);
  
  fp.close()
  # print("Some nonsense\n")



if __name__ == "__main__":
  main()
 