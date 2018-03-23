import grpc
import time

from common import PORT
from proto.service_pb2 import Request
from proto.service_pb2_grpc import TestServiceStub


def channel_update_monitor(state):
    print(state)


def make_client():
    channel = grpc.insecure_channel('localhost:{}'.format(PORT))
    channel.subscribe(channel_update_monitor)
    stub = TestServiceStub(channel)
    return stub


def make_requests(client):
    req = iter([Request(id=1)])
    resp = client.StreamStream(req)
    import time
    time.sleep(1)
    next(resp)
    try:
        next(resp)
    except grpc.RpcError as e:
        assert e.code() == grpc.StatusCode.UNKNOWN


if __name__ == '__main__':
    make_requests(make_client())
