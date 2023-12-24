import grpc
import example_pb2
import example_pb2_grpc
import time
import os 
import json

class Customer:
    def __init__(self, id, events):
        self.id = id
        self.events = events
        self.recvMsg = [] 
        self.stub = None 
        
    def createStub(self, bank_address):
        channel = grpc.insecure_channel(bank_address, options=(('grpc.enable_http_proxy', 0),))
        self.stub = example_pb2_grpc.RPCStub(channel)

    def executeEvents(self):
        responses = []
        loc_clock = 0
        for event in self.events:
            loc_clock += 1
            if event["interface"] == "query":
                request = example_pb2.BankingEvent(id=self.id, interface=event["interface"])
                response = self.stub.MsgDelivery(request)
                responses.append({'interface':"query", 'balance':response.result})
                a = []
                out_file = {'interface':"query", 'balance':response.result}
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
            else:
                responses.append({'customer-request-id': event["customer-request-id"], 'logical_clock':loc_clock, 'interface':event["interface"], 'comment':"event_sent from customer "+str(self.id)})
                a = []
                out_file = {'id':self.id, 'customer-request-id': event["customer-request-id"], 'type':'customer', 'logical_clock':loc_clock, 'interface':event["interface"], 'comment':"event_sent from customer "+str(self.id)}
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
                request = example_pb2.BankingEvent(id=self.id, interface=event["interface"], money=event["money"], clock = loc_clock)
                response = self.stub.MsgDelivery(request)
        a = []
        out_file = {'id': self.id, 'type':"customer", 'events':responses}
        fname = "output_1.json"
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
      
