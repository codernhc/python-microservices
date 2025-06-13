from fastapi import APIRouter
from starlette.responses import JSONResponse

from biz.hello import say_hello
from server.channel import get_channel
from protos.hello_pb2 import HelloRequest
from protos.hello_pb2_grpc import HelloStub

router = APIRouter()

channel = get_channel()
hello_stub = HelloStub(channel)


@router.get("")
async def hello(
  message: str = "[http]: test"
):
  result = say_hello(message)

  return JSONResponse(
    status_code=200,
    content={"message": result}
  )


@router.get("/rpc.client")
async def hello1(
  message: str = "[http rpc-client]: test"
):
  print(f"[http rpc-client]: {message}")
  result = hello_stub.SayHello(HelloRequest(name=message))

  return JSONResponse(
    status_code=200,
    content={"message": result.message}
  )
