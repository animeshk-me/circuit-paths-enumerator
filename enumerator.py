#*****************************************************************#
'''
The Main Module which drives all the code.
'''
#*****************************************************************#

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
  
  # convert the cicuit gates information into python list of objects
  gate_data = get_gates_data(fp)
  fp.close() # close files
  
  # transforming the gate-data into a graph
  final_graph = get_final_graph(gate_data, input_list, output_list)  
  final_graph.print_graph("Final")

  # enumerate all possible paths from Inputs to outputs and print
  print("All paths from inputs to outputs:\n")
  all_paths = get_final_paths(input_list, output_list, final_graph)
  print(*all_paths, sep="\n")
  print("Total number of paths:", len(all_paths))


# Entry point
if __name__ == "__main__":
  main()
 
#*****************************************************************#
