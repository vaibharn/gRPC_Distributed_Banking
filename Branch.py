import grpc
import example_pb2
import example_pb2_grpc
from concurrent import futures 
import time 

class Branch(example_pb2_grpc.RPCServicer):

    def __init__(self, id, balance, branches):
        self.id = id
        self.balance = balance
        self.stubList = []  # List to store client stubs for communication with other branches
        self.recvMsg = []  # List to store received messages for debugging
        self.branches = branches
        self.flag = 0
        
    # Method to process requests from both clients and branches
    def MsgDelivery(self, request, context):  
        res = ""
        if request.interface == "withdraw":
            return self.withdraw(request, context)
        elif request.interface == "deposit":
            return self.deposit(request, context)
            request = example_pb2.NewBalance(updatedbalance = self.balance)
        else:
            return self.query(request, context)
        
    def query(self, request, context):
        while self.flag == 1:
            time.sleep(1)
        return example_pb2.Response(id = self.id, result = str(self.balance))
    
    def deposit(self, request, context):
        while self.flag == 1:
            time.sleep(1)
        self.balance += request.money
        for branch in self.branches:
            if branch != self.id:
                port = 7000 + branch
                channel = grpc.insecure_channel("localhost:"+str(port), options=(('grpc.enable_http_proxy', 0),))
                stub = example_pb2_grpc.RPCStub(channel)
                response = stub.PropagateDeposit(example_pb2.NewBalance(updatedbalance = self.balance))
        return example_pb2.Response(id = self.id, result = "success")
    
    def withdraw(self, request,context):
        while self.flag == 1:
            time.sleep(1)
        if self.balance >= request.money:
            self.balance -= request.money
            for branch in self.branches:
                if branch != self.id:
                    port = 7000 + branch
                    channel = grpc.insecure_channel("localhost:"+str(port), options=(('grpc.enable_http_proxy', 0),))
                    stub = example_pb2_grpc.RPCStub(channel)
                    response = stub.PropagateWithdraw(example_pb2.NewBalance(updatedbalance = self.balance))
            return example_pb2.Response(id = self.id, result = "success")
        else:
            return example_pb2.Response(id = self.id, result = "fail")
    
    def PropagateDeposit(self, request, context):
        self.flag = 1
        self.balance = request.updatedbalance
        self.flag = 0
        return example_pb2.PropagateResp(resp = "success")
    
    def PropagateWithdraw(self, request, context):
        self.flag = 1
        self.balance = request.updatedbalance
        self.flag = 0
        return example_pb2.PropagateResp(resp = "success")

    def start(self):
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        example_pb2_grpc.add_RPCServicer_to_server(self, server)
        port = 7000 + int(self.id)
        server.add_insecure_port('[::]:'+str(port))
        server.start()
        server.wait_for_termination()

