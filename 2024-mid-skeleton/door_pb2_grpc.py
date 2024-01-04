# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import door_pb2 as door__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class DoorStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ProcessEvent = channel.unary_unary(
                '/Door/ProcessEvent',
                request_serializer=door__pb2.Event.SerializeToString,
                response_deserializer=door__pb2.Response.FromString,
                )
        self.GetCurrentState = channel.unary_unary(
                '/Door/GetCurrentState',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=door__pb2.CurrentStateResponse.FromString,
                )


class DoorServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ProcessEvent(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCurrentState(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DoorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ProcessEvent': grpc.unary_unary_rpc_method_handler(
                    servicer.ProcessEvent,
                    request_deserializer=door__pb2.Event.FromString,
                    response_serializer=door__pb2.Response.SerializeToString,
            ),
            'GetCurrentState': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCurrentState,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=door__pb2.CurrentStateResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Door', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Door(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ProcessEvent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Door/ProcessEvent',
            door__pb2.Event.SerializeToString,
            door__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetCurrentState(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Door/GetCurrentState',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            door__pb2.CurrentStateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
