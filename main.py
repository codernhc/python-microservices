import os
import sys
import grpc
import threading
from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from concurrent import futures

PROTO_DIR = os.path.join(os.path.dirname(__file__), "protos")
sys.path.insert(0, PROTO_DIR)
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from services.hello import Hello
from protos.hello_pb2_grpc import add_HelloServicer_to_server


def run_grpc():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  add_HelloServicer_to_server(Hello(), server)
  server.add_insecure_port('[::]:50051')
  server.start()
  print("gRPC Server started on port 50051")
  server.wait_for_termination()


@asynccontextmanager
async def lifespan(app: FastAPI):
  grpc_thread = threading.Thread(target=run_grpc, daemon=True)
  grpc_thread.start()
  print("gRPC service started in background")
  yield


app = FastAPI(lifespan=lifespan)

app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

from api.v1.hello.route import router as hello_router

app.include_router(hello_router, prefix="/api/v1/hello")

if __name__ == "__main__":
  import uvicorn

  uvicorn.run(app, host="0.0.0.0", port=3000)
