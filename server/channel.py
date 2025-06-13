import grpc

channel = grpc.insecure_channel("localhost:50051")


def get_channel():
  return channel
