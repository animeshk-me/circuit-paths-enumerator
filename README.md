# Circuit to Graph

## Overview of the Project
* This is a python script which reads and parses a verilog file as input
* Then it creates a directed acyclic graph(DAG) to represent the equivalent combinational circuit.
* We use python dictionaries to represent the DAG in the form of an Adjacency list.
* Then it enumerates all the possible paths from the circuit inputs to outputs recursively.
* The graph algorithm **Breadth First Search(BFS)** is used for this purpose.

## Execution method:
* Run this command

      $ python3 enumerator.py
* A prompt opens, enter the details
    ```js
    $ Enter a valid verilog file name: <filename>
    ```           

**PS:** *This script accepts information(.v file) in a certain format. That shall be specified later*
