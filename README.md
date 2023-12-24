# gRPC Distributed Banking

The objective of this project is to enhance the coordination and synchronization among the customer and branch processes for the distributed banking system created in Project 1. The current system lacks a robust mechanism for maintaining a consistent order of events across these processes, leading to potential inconsistencies and difficulties in tracking the sequence of operations.


The following technologies were used in making of this project:
•	Python
•	gRPC
•	Protobuf by Google
•	Python virtual enviornment
To run this project you will need a python environment with the following packages installed:
•	grpc
•	grpcio


Use the following command to generate the Python code for protobuf:

```python
python -m grpc_tools.protoc -I. --python_out=. --pyi_out=. --grpc_python_out=. .example.proto
```


To run the program make sure that the input.json is in the same folder as main.py then execute the following command:
````
python main.py
````


The output file is generated as output.json in the same folder.
