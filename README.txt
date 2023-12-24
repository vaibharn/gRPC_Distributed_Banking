Use the following command to generate the Python code for protobuf:
python -m grpc_tools.protoc -I. --python_out=. --pyi_out=. --grpc_python_out=. .example.proto

To run the program make sure that the input.json is in the same folder as main.py then execute the following command:

python main.py

The output file is generated as output.json in the same folder.
