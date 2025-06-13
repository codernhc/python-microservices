import os
import sys
import grpc
import logging
from concurrent import futures

PROTO_DIR = os.path.join(os.path.dirname(__file__), "protos")
sys.path.insert(0, PROTO_DIR)
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from services.hello import Hello
from protos.hello_pb2_grpc import add_HelloServicer_to_server


def serve():
  port = "50051"
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  add_HelloServicer_to_server(Hello(), server)
  server.add_insecure_port("[::]:" + port)
  server.start()
  server.wait_for_termination()


if __name__ == "__main__":
  logging.basicConfig()
  serve()
