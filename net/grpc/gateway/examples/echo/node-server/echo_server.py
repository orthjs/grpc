"""The Python implementation of the gRPC route guide server."""
from concurrent import futures
import logging
import math
import time
import grpc
import echo_pb2
import echo_pb2_grpc

class EchoServiceServicer(echo_pb2_grpc.EchoServiceServicer):

    def Echo(self, request, context):
        print(request.message)
        return echo_pb2.EchoResponse(message="87", message_count=87)

    def ServerStreamingEcho(self, request, context):
        for i in range(request.message_count):
            yield echo_pb2.ServerStreamingEchoResponse(message="123")
            time.sleep(request.message_interval)
            
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    print("123")
    echo_pb2_grpc.add_EchoServiceServicer_to_server(
        EchoServiceServicer(), server)
    server.add_insecure_port('127.0.0.1:9090')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
