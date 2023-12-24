# gRPC Distributed Banking

This project aims to enhance the existing Project 1 by implementing a client-centric consistency model for the distributed banking system. The primary objective is to develop essential functions that enforce the read-your-writes consistency model, ensuring coherence in replicated data across the bank. The key tasks involve tracking read and write events by the same customer across various branch processes and implementing read-your-writes consistency among these processes. The project addresses the challenge of maintaining data consistency as customers change branches while submitting requests to the bank.


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
