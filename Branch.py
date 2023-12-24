import grpc
import example_pb2
import example_pb2_grpc
from concurrent import futures 
import time 
import json
import os 

class Branch(example_pb2_grpc.RPCServicer):

    def __init__(self, id, balance, branches):
        self.id = id
        self.balance = balance
        self.stubList = [] 
        self.recvMsg = []  
        self.branches = branches
        self.loc_clock = 0
        self.output_2 = []


    def MsgDelivery(self, request, context):  
        res = ""
        self.loc_clock = max(self.loc_clock, request.clock) + 1
        self.output_2.append({'customer-request-id':request.id, 'logical_clock':self.loc_clock, 'interface':request.interface, 'comment':"event_recv from customer " + str(request.id)})
        a = []
        out_file = {'id':self.id, 'customer-request-id':request.id, 'type':'branch', 'logical_clock':self.loc_clock, 'interface':request.interface, 'comment':"event_recv from customer " + str(request.id)}
        fname = "output_3.json"
        if not os.path.isfile(fname):
            a.append(out_file)
            with open(fname, mode='w') as f:
                f.write(json.dumps(a, indent=2))
        else:
            with open(fname, encoding='utf-8') as feedsjson:
                feeds = json.load(feedsjson)

            feeds.append(out_file)
            with open(fname, mode='w') as f:
                f.write(json.dumps(feeds, indent=2)) 

        if request.interface == "withdraw":
            return self.withdraw(request, context)
        elif request.interface == "deposit":
            return self.deposit(request, context)
        else:
            return self.query(request, context)
        
    def query(self, request, context):
        return example_pb2.Response(id = self.id, result = str(self.balance))
    
    def deposit(self, request, context):
        self.balance += request.money
        for branch in self.branches:
            if branch != self.id:
                self.loc_clock += 1
                self.output_2.append({'customer-request-id':request.id, 'logical_clock':self.loc_clock, 'interface':"propagate_deposit", 'comment':"event_sent to branch " + str(branch)})
                a = []
                out_file = {'id':self.id, 'customer-request-id':request.id, 'type':'branch', 'logical_clock':self.loc_clock, 'interface':"propagate_deposit", 'comment':"event_sent to branch " + str(branch)}
                fname = "output_3.json"
                if not os.path.isfile(fname):
                    a.append(out_file)
                    with open(fname, mode='w') as f:
                        f.write(json.dumps(a, indent=2))
                else:
                    with open(fname, encoding='utf-8') as feedsjson:
                        feeds = json.load(feedsjson)

                    feeds.append(out_file)
                    with open(fname, mode='w') as f:
                        f.write(json.dumps(feeds, indent=2))
                port = 7000 + branch
                channel = grpc.insecure_channel("localhost:"+str(port), options=(('grpc.enable_http_proxy', 0),))
                stub = example_pb2_grpc.RPCStub(channel)
                response = stub.PropagateDeposit(example_pb2.NewBalance(clock = self.loc_clock, updatedbalance = self.balance, id = self.id))
        return example_pb2.Response(id = self.id, result = "success")
    
    def withdraw(self, request,context):
        if self.balance >= request.money:
            self.balance -= request.money
            for branch in self.branches:
                if branch != self.id:
                    self.loc_clock += 1
                    self.output_2.append({'customer-request-id':request.id, 'logical_clock':self.loc_clock, 'interface':"propagate_withdraw", 'comment':"event_sent to branch " + str(branch)})
                    a = []
                    out_file = {'id':self.id, 'customer-request-id':request.id, 'type':'branch', 'logical_clock':self.loc_clock, 'interface':"propagate_withdraw", 'comment':"event_sent to branch " + str(branch)}
                    fname = "output_3.json"
                    if not os.path.isfile(fname):
                        a.append(out_file)
                        with open(fname, mode='w') as f:
                            f.write(json.dumps(a, indent=2))
                    else:
                        with open(fname, encoding='utf-8') as feedsjson:
                            feeds = json.load(feedsjson)

                        feeds.append(out_file)
                        with open(fname, mode='w') as f:
                            f.write(json.dumps(feeds, indent=2))
                    port = 7000 + branch
                    channel = grpc.insecure_channel("localhost:"+str(port), options=(('grpc.enable_http_proxy', 0),))
                    stub = example_pb2_grpc.RPCStub(channel)
                    response = stub.PropagateWithdraw(example_pb2.NewBalance(clock = self.loc_clock, updatedbalance = self.balance, id = self.id))
            return example_pb2.Response(id = self.id, result = "success")
        else:
            return example_pb2.Response(id = self.id, result = "fail")
    
    def PropagateDeposit(self, request, context):
        self.balance = request.updatedbalance
        self.loc_clock = max(self.loc_clock, request.clock) + 1
        self.output_2.append({'customer-request-id':request.id, 'logical_clock':self.loc_clock, 'interface':"propagate_deposit", 'comment':"event_recv from branch " + str(request.id)})
        a = []
        out_file = {'id':self.id, 'customer-request-id':request.id, 'type':'branch', 'logical_clock':self.loc_clock, 'interface':"propagate_deposit", 'comment':"event_recv from branch " + str(request.id)}
        fname = "output_3.json"
        if not os.path.isfile(fname):
            a.append(out_file)
            with open(fname, mode='w') as f:
                f.write(json.dumps(a, indent=2))
        else:
            with open(fname, encoding='utf-8') as feedsjson:
                feeds = json.load(feedsjson)

            feeds.append(out_file)
            with open(fname, mode='w') as f:
                f.write(json.dumps(feeds, indent=2))          
        return example_pb2.PropagateResp(resp = "success")
    
    def PropagateWithdraw(self, request, context):
        self.balance = request.updatedbalance
        self.loc_clock = max(self.loc_clock, request.clock) + 1
        self.output_2.append({'customer-request-id':request.id, 'logical_clock':self.loc_clock, 'interface':"propagate_withdraw", 'comment':"event_recv from branch " + str(request.id)})
        a = []
        out_file = {'id':self.id, 'customer-request-id':request.id, 'type':'branch', 'logical_clock':self.loc_clock, 'interface':"propagate_withdraw", 'comment':"event_recv from branch " + str(request.id)}
        fname = "output_3.json"
        if not os.path.isfile(fname):
            a.append(out_file)
            with open(fname, mode='w') as f:
                f.write(json.dumps(a, indent=2))
        else:
            with open(fname, encoding='utf-8') as feedsjson:
                feeds = json.load(feedsjson)

            feeds.append(out_file)
            with open(fname, mode='w') as f:
                f.write(json.dumps(feeds, indent=2))  
        return example_pb2.PropagateResp(resp = "success")

    def start(self):
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        example_pb2_grpc.add_RPCServicer_to_server(self, server)
        port = 7000 + int(self.id)
        server.add_insecure_port('[::]:'+str(port))
        server.start()
        server.wait_for_termination(1+(self.id * 0.1))
        print("Branch ", self.id, "terminated")
        a = []
        out_file = {'id':self.id, 'type':"branch", 'events':self.output_2}
        fname = "output_2.json"
        if not os.path.isfile(fname):
            a.append(out_file)
            with open(fname, mode='w') as f:
                f.write(json.dumps(a, indent=2))
        else:
            with open(fname, encoding='utf-8') as feedsjson:
                feeds = json.load(feedsjson)

            feeds.append(out_file)
            with open(fname, mode='w') as f:
                f.write(json.dumps(feeds, indent=2)) 

