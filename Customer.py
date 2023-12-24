import grpc
import example_pb2
import example_pb2_grpc
import time

class Customer:
    def __init__(self, id, events):
        self.id = id
        self.events = events
        self.recvMsg = [] 
        self.stub = None 
        
    def createStub(self, bank_address):
        channel = grpc.insecure_channel(bank_address, options=(('grpc.enable_http_proxy', 0),))
        self.stub = example_pb2_grpc.RPCStub(channel)

    # Method to send out the events to the Bank
    def executeEvents(self):
        # Iterate through events and send them to the Bank
        responses = []
        for event in self.events:
            # Prepare gRPC request based on your example_pb2 Event message
            port = 7000 + int(event["branch"])
            self.createStub("localhost:"+str(port))  # Replace with actual branch address
            if event["interface"] == "query":
                request = example_pb2.BankingEvent(id=self.id, interface=event["interface"])
                response = self.stub.MsgDelivery(request)
                responses.append({'id': self.id, 'recv':[{'interface':"query", 'branch': event["branch"], 'balance':response.result}]})
            else:
                request = example_pb2.BankingEvent(id=self.id, interface=event["interface"], money=event["money"])
                response = self.stub.MsgDelivery(request)
                responses.append({'id': self.id, 'recv':[{'interface':event["interface"], 'branch': event["branch"], 'result':response.result}]})
        return responses
