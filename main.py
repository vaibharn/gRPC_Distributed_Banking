import json
from multiprocessing import Process
from concurrent.futures import ThreadPoolExecutor
from Customer import Customer
from Branch import Branch
import time
import os 

def process_customer(customer_info, id):
    customer = Customer(customer_info["id"], customer_info["customer-requests"])
    port = 7000 + int(customer_info["id"])
    customer.createStub("localhost:"+str(port))
    customer.executeEvents()

def create_branch(branch_info, branches):
    branch = Branch(branch_info["id"], branch_info["balance"], branches)
    branch.start()

if __name__ == "__main__":
    with open('input_10.json', 'r') as file:
        data = json.load(file)

    if os.path.isfile("output_1.json"):
        os.remove("output_1.json")

    if os.path.isfile("output_2.json"):
        os.remove("output_2.json")

    if os.path.isfile("output_3.json"):
        os.remove("output_3.json")

    processes_branch = []
    processes_customer = []
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
            process = Process(target=process_customer, args = (item, item["id"]))
            processes_customer.append(process)
            process.start()
            process.join()
    
    for process in processes_customer:
       process.join()

    for process in processes_branch:
       process.join()
    
    print("output_1.json generated")
    print("output_2.json generated")
    print("output_3.json generated")
    print("END")
 
