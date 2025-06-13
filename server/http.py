import os
import sys

from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware

PROTO_DIR = os.path.join(os.path.dirname(__file__), "protos")
sys.path.insert(0, PROTO_DIR)
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from api.v1.hello.route import router as hello_router

app = FastAPI()


@asynccontextmanager
async def lifespan(_app: FastAPI):
  print("")


app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

app.include_router(hello_router, prefix="/api/v1/hello")

if __name__ == "__main__":
  import uvicorn

  uvicorn.run(app, host="0.0.0.0", port=3000)
