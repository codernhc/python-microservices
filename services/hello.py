# service层：rpc 服务

from biz.hello import say_hello
from protos.hello_pb2_grpc import HelloServicer
from protos.hello_pb2 import HelloReply


class Hello(HelloServicer):
  def SayHello(self, request, context):
    result = say_hello(f"from rpc server: {request.name}")
    return HelloReply(message=result)
