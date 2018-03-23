import grpc
import time
import concurrent.futures as futures

from common import PORT
from proto.service_pb2_grpc import TestServiceServicer, add_TestServiceServicer_to_server
from proto.service_pb2 import Response


class TestServicer(TestServiceServicer):

    def UnaryUnary(self, request, context):
        raise Exception("TODO")

    def UnaryStream(self, request, context):
        raise Exception("TODO")

    def StreamUnary(self, request_iterator, context):
        raise Exception("TODO")

    def StreamStream(self, request_iterator, context):
        yield Response(response=1)
        raise Exception()


def make_server(port):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_TestServiceServicer_to_server(TestServicer(), server)
    server.add_insecure_port('localhost:{}'.format(port))
    return server


if __name__ == '__main__':

    server = make_server(PORT)
    try:
        server.start()
        while True:
            time.sleep(60 * 60 * 24)
    except KeyboardInterrupt:
        server.stop(0)
