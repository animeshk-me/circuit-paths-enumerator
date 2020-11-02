from parser import (
  get_input_list,
  get_output_list,
  get_gates_data,
)

from graph_methods import (
  get_final_graph,
  get_final_paths
)

# Main function
def main():
  filename = input("Enter a valid verilog file name: ")
  try:
    fp = open(filename, "r")
  except FileNotFoundError:
    print("The file name entered doesn't exist.\nPlease try again...")
    return
  
  # convert the circuit I/O info into python list
  input_list = get_input_list(fp)
  output_list = get_output_list(fp)
  print("Overall inputs", input_list)
  print("Overall outputs", output_list)
  
  # convert the cicuit gates into
  gate_data = get_gates_data(fp);
  for gate in gate_data:
    print(gate.name, gate.inputs, gate.output)
  fp.close() # close files
  
  # converting the data into a graph
  final_graph = get_final_graph(gate_data, input_list, output_list)  
  final_graph.print_graph("Final")

  # enumerate all possible path from Inputs to outputs and print
  all_paths = get_final_paths(input_list, output_list, final_graph)
  print(*all_paths, sep="\n")


# Entry point
if __name__ == "__main__":
  main()
 