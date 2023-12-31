# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import example_pb2 as example__pb2


class RPCStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.MsgDelivery = channel.unary_unary(
                '/RPC/MsgDelivery',
                request_serializer=example__pb2.BankingEvent.SerializeToString,
                response_deserializer=example__pb2.Response.FromString,
                )
        self.PropagateDeposit = channel.unary_unary(
                '/RPC/PropagateDeposit',
                request_serializer=example__pb2.NewBalance.SerializeToString,
                response_deserializer=example__pb2.PropagateResp.FromString,
                )
        self.PropagateWithdraw = channel.unary_unary(
                '/RPC/PropagateWithdraw',
                request_serializer=example__pb2.NewBalance.SerializeToString,
                response_deserializer=example__pb2.PropagateResp.FromString,
                )


class RPCServicer(object):
    """Missing associated documentation comment in .proto file."""

    def MsgDelivery(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PropagateDeposit(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PropagateWithdraw(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RPCServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'MsgDelivery': grpc.unary_unary_rpc_method_handler(
                    servicer.MsgDelivery,
                    request_deserializer=example__pb2.BankingEvent.FromString,
                    response_serializer=example__pb2.Response.SerializeToString,
            ),
            'PropagateDeposit': grpc.unary_unary_rpc_method_handler(
                    servicer.PropagateDeposit,
                    request_deserializer=example__pb2.NewBalance.FromString,
                    response_serializer=example__pb2.PropagateResp.SerializeToString,
            ),
            'PropagateWithdraw': grpc.unary_unary_rpc_method_handler(
                    servicer.PropagateWithdraw,
                    request_deserializer=example__pb2.NewBalance.FromString,
                    response_serializer=example__pb2.PropagateResp.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'RPC', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RPC(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def MsgDelivery(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/RPC/MsgDelivery',
            example__pb2.BankingEvent.SerializeToString,
            example__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PropagateDeposit(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/RPC/PropagateDeposit',
            example__pb2.NewBalance.SerializeToString,
            example__pb2.PropagateResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PropagateWithdraw(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/RPC/PropagateWithdraw',
            example__pb2.NewBalance.SerializeToString,
            example__pb2.PropagateResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
