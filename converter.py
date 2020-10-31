from classes import Gate

def Str2Gate(str):
  if str[0:2] == "or":
  elif str[0:3] == "and":
  elif str[0:3] == "not":
  elif str[0:3] == "nor":
  elif str[0:3] == "xor":
  elif str[0:4] == "xnor":
  elif str[0:4] == "nand":
  else:
    return -1;

def get_gates_data(fp):
  content = fp.readlines()
  fp.seek(0);
  gates_list = []
  for line in content:
    if(line[0:9] == "endmodule")
      break;
    gate_data = Str2Gate(line);
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
 