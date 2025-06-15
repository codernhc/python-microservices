import os
import sys
import threading
from fastapi import FastAPI

PROTO_DIR = os.path.join(os.path.dirname(__file__), "protos")
sys.path.insert(0, PROTO_DIR)
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from contextlib import asynccontextmanager
from server.grpc_server import GrpcServer
from server.http_server import HttpServer

grpc_server = GrpcServer()


@asynccontextmanager
async def lifespan(app: FastAPI):
  grpc_thread = threading.Thread(target=grpc_server.start(), daemon=True)
  grpc_thread.start()
  print("gRPC service started in background")
  yield


http_server = HttpServer(lifespan=lifespan)

if __name__ == "__main__":
  http_server.start()
