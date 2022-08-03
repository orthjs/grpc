"""The Python implementation of the gRPC route guide client."""

from __future__ import print_function

import logging
import random

import grpc
import echo_pb2
import echo_pb2_grpc

def serverstreamingEcho(stub):
    features = stub.ServerStreamingEcho(echo_pb2.ServerStreamingEchoRequest(message="159", message_count = 10, message_interval = 3))
    for feature in features:
        print("Feature called %s" % (feature.message))

def guide_get_one_feature(stub):
    feature = stub.Echo(echo_pb2.EchoRequest(message = "123"))
    print("Feature called %s" % (feature.message))

def run():

    with grpc.insecure_channel('localhost:9090') as channel:
        stub = echo_pb2_grpc.EchoServiceStub(channel)
        print("-------------- GetFeature --------------")
        guide_get_one_feature(stub)
        print("----------------------------------------")
        serverstreamingEcho(stub)
        
if __name__ == '__main__':
    logging.basicConfig()
    run()
