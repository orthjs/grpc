FROM python:3

WORKDIR /github/grpc-web/net/grpc/gateway/examples/echo/node-server

COPY net/grpc/gateway/examples/echo/node-server/requirements.txt ./
COPY net/grpc/gateway/examples/echo/node-server/echo_server.py .
COPY net/grpc/gateway/examples/echo/node-server/echo_pb2.py .
COPY net/grpc/gateway/examples/echo/node-server/echo_pb2_grpc.py .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 9090
CMD ["python", "./echo_server.py"]
