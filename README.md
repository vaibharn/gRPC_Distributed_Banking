# gRPC Distributed Banking

The problem statement is to develop a distributed banking system that enables numerous customers to conduct withdrawals and deposits across various branches within the bank. It is presumed that all customers share a common bank account, and each customer is linked to a specific branch for their transactions. Furthermore, the project operates under the assumption that concurrent updates to the bank account do not occur. Each branch is responsible for maintaining a copy of the funds, which must remain synchronized with the copies held in other branches. To facilitate this, each customer exclusively interacts with the branch identified by their unique ID. Although each customer independently updates a designated replica, it is essential for all replicas stored in every branch to accurately reflect the cumulative updates made by the customer.


The following technologies were used in making of this project:
•	Python
•	gRPC
•	Protobuf by Google
•	Python virtual enviornment
To run this project you will need a python environment with the following packages installed:
•	grpc
•	grpcio
Use the following command to generate the Python code for protobuf:
python -m grpc_tools.protoc -I. --python_out=. --pyi_out=. --grpc_python_out=. .example.proto

To run the program make sure that the input.json is in the same folder as main.py then execute the following command:

python main.py

The output file is generated as output.json in the same folder.
