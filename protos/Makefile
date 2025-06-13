PROTO_DIR = ./
OUTPUT_DIR = ./

PROTO_FILES := $(wildcard $(PROTO_DIR)/*.proto)


proto-py:
	@for file in $(PROTO_FILES); do \
		echo "Processing $$file"; \
		python -m grpc_tools.protoc -I$(PROTO_DIR) --python_out=$(OUTPUT_DIR) --pyi_out=$(OUTPUT_DIR) --grpc_python_out=$(OUTPUT_DIR) "$$file"; \
	done

all: proto-py