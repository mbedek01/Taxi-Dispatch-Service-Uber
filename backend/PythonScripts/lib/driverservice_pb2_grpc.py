# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import lib.driverservice_pb2 as driverservice__pb2


class DriverServiceStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.StoreUserLogin = channel.unary_unary(
            '/proto.DriverService/StoreUserLogin',
            request_serializer=driverservice__pb2.User.SerializeToString,
            response_deserializer=driverservice__pb2.Response.FromString,
        )
        self.UpdateLocation = channel.unary_unary(
            '/proto.DriverService/UpdateLocation',
            request_serializer=driverservice__pb2.LocationRequest.SerializeToString,
            response_deserializer=driverservice__pb2.Response.FromString,
        )
        self.GetDriverInLocation = channel.unary_unary(
            '/proto.DriverService/GetDriverInLocation',
            request_serializer=driverservice__pb2.GetLocationRequest.SerializeToString,
            response_deserializer=driverservice__pb2.DriverDetails.FromString,
        )


class DriverServiceServicer(object):
    """Missing associated documentation comment in .proto file"""

    def StoreUserLogin(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateLocation(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDriverInLocation(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DriverServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'StoreUserLogin': grpc.unary_unary_rpc_method_handler(
            servicer.StoreUserLogin,
            request_deserializer=driverservice__pb2.User.FromString,
            response_serializer=driverservice__pb2.Response.SerializeToString,
        ),
        'UpdateLocation': grpc.unary_unary_rpc_method_handler(
            servicer.UpdateLocation,
            request_deserializer=driverservice__pb2.LocationRequest.FromString,
            response_serializer=driverservice__pb2.Response.SerializeToString,
        ),
        'GetDriverInLocation': grpc.unary_unary_rpc_method_handler(
            servicer.GetDriverInLocation,
            request_deserializer=driverservice__pb2.GetLocationRequest.FromString,
            response_serializer=driverservice__pb2.DriverDetails.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'proto.DriverService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class DriverService(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def StoreUserLogin(request,
                       target,
                       options=(),
                       channel_credentials=None,
                       call_credentials=None,
                       compression=None,
                       wait_for_ready=None,
                       timeout=None,
                       metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.DriverService/StoreUserLogin',
                                             driverservice__pb2.User.SerializeToString,
                                             driverservice__pb2.Response.FromString,
                                             options, channel_credentials,
                                             call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateLocation(request,
                       target,
                       options=(),
                       channel_credentials=None,
                       call_credentials=None,
                       compression=None,
                       wait_for_ready=None,
                       timeout=None,
                       metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.DriverService/UpdateLocation',
                                             driverservice__pb2.LocationRequest.SerializeToString,
                                             driverservice__pb2.Response.FromString,
                                             options, channel_credentials,
                                             call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDriverInLocation(request,
                            target,
                            options=(),
                            channel_credentials=None,
                            call_credentials=None,
                            compression=None,
                            wait_for_ready=None,
                            timeout=None,
                            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.DriverService/GetDriverInLocation',
                                             driverservice__pb2.GetLocationRequest.SerializeToString,
                                             driverservice__pb2.DriverDetails.FromString,
                                             options, channel_credentials,
                                             call_credentials, compression, wait_for_ready, timeout, metadata)
