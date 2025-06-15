import os
import sys
import grpc
import logging
from concurrent import futures
from services.hello import Hello
from protos.hello_pb2_grpc import add_HelloServicer_to_server

class GrpcServer:
  def __init__(self, port="50051"):
    self.port = port
    self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

  def start(self):
    logging.basicConfig()
    self.register_service()
    self.server.add_insecure_port("[::]:" + self.port)
    self.server.start()
    print("Server started, listening on " + self.port)
    # self.server.wait_for_termination()

  def register_service(self):
    add_HelloServicer_to_server(Hello(), self.server)


if __name__ == "__main__":
  PROTO_DIR = os.path.join(os.path.dirname(__file__), "../protos")
  sys.path.insert(0, PROTO_DIR)
  sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

  from services.hello import Hello
  from protos.hello_pb2_grpc import add_HelloServicer_to_server

  server = GrpcServer()
  server.start()
