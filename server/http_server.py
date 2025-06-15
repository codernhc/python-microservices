import os
import sys

from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from api.v1.hello.route import router as hello_router


class HttpServer:
  def __init__(self, lifespan=None):
    self.app = FastAPI(lifespan=lifespan if lifespan else self.app_lifespan)
    self._setup_middleware()
    self.app.include_router(hello_router, prefix="/api/v1/hello")

  def _setup_middleware(self):
    self.app.add_middleware(
      CORSMiddleware,
      allow_origins=["*"],
      allow_credentials=True,
      allow_methods=["*"],
      allow_headers=["*"],
    )

  @asynccontextmanager
  async def app_lifespan(self, _app: FastAPI):
    print("Server is starting...")
    yield
    print("Server is shutting down...")

  def start(self):
    import uvicorn

    uvicorn.run(self.app, host="0.0.0.0", port=3000)


if __name__ == "__main__":
  PROTO_DIR = os.path.join(os.path.dirname(__file__), "../protos")
  sys.path.insert(0, PROTO_DIR)
  sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

  from api.v1.hello.route import router as hello_router

  http_server = HttpServer()

  http_server.start()
