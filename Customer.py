import grpc
import example_pb2
import example_pb2_grpc
import time

#Customer class
class Customer:
    def __init__(self, id, events):
        self.id = id
        self.events = events 
        self.stub = None 

    #Creating a stub for communication through gRPC
    def createStub(self, bank_address):
        channel = grpc.insecure_channel(bank_address, options=(('grpc.enable_http_proxy', 0),))
        self.stub = example_pb2_grpc.RPCStub(channel)

    # Method to send out the events to the Branches
    def executeEvents(self):
        # Iterate through events and send them to the Branches
        responses = []
        for event in self.events:
            # Prepare gRPC request based on your example_pb2 BankingEvent message
            if event["interface"] == "query":
                request = example_pb2.BankingEvent(id=self.id, interface=event["interface"])
                response = self.stub.MsgDelivery(request)
                responses.append({'interface':"query", 'balance':response.result})
            else:
                request = example_pb2.BankingEvent(id=self.id, interface=event["interface"], money=event["money"])
                response = self.stub.MsgDelivery(request)
                responses.append({'interface':event["interface"], 'result':response.result})
        return responses
