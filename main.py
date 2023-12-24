import json
from multiprocessing import Process
from Customer import Customer
from Branch import Branch
import time

#function for processing customers
def process_customer(customer_info):
    customer = Customer(customer_info["id"], customer_info["events"])
    port = 7000 + int(customer_info["id"])
    customer.createStub("localhost:"+str(port))  # Replace with actual branch address
    out = customer.executeEvents()
    return out

#fucntion to create branches
def create_branch(branch_info, branches):
    branch = Branch(branch_info["id"], branch_info["balance"], branches)
    branch.start()

if __name__ == "__main__":
    #Read input file
    with open('input.json', 'r') as file:
        data = json.load(file)

    processes_branch = []
    branches = []

    #storing all branches with their IDs
    for item in data:
        if item["type"] == "branch":
            branches.append(item["id"])

    #Start all branch processes
    for item in data:
        if item["type"] == "branch":
            process = Process(target=create_branch, args=(item, branches))
            processes_branch.append(process)
            process.start()

    
    output = []

    #Start all customer processes
    for item in data:
        if item["type"] == "customer":
            response = process_customer(item)
            output.append({'id': item["id"], 'recv':response})

    #Create output file            
    with open('output.json', 'w') as file:
        json.dump(output, file, indent=1)
    print("output.json generated")

    for process in processes_branch:
       process.join()

