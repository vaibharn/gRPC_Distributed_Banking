import json
from multiprocessing import Process
from Customer import Customer
from Branch import Branch
import time

def process_customer(customer_info):
    customer = Customer(customer_info["id"], customer_info["events"])
    out = customer.executeEvents()
    return out

def create_branch(branch_info, branches):
    branch = Branch(branch_info["id"], branch_info["balance"], branches)
    branch.start()

if __name__ == "__main__":
    with open('input_big.json', 'r') as file:
        data = json.load(file)

    processes_branch = []
    branches = []

    for item in data:
        if item["type"] == "branch":
            branches.append(item["id"])

    for item in data:
        if item["type"] == "branch":
            process = Process(target=create_branch, args=(item, branches))
            processes_branch.append(process)
            process.start()

    
    for item in data:
        if item["type"] == "customer":
            response = process_customer(item)
           
    with open('output.json', 'w') as file:
        json.dump(response, file, indent=1)
    print("output.json generated")
    
    for process in processes_branch:
       process.join()

