# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: echo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\necho.proto\x12\x14grpc.gateway.testing\"\x07\n\x05\x45mpty\"\x1e\n\x0b\x45\x63hoRequest\x12\x0f\n\x07message\x18\x01 \x01(\t\"6\n\x0c\x45\x63hoResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x15\n\rmessage_count\x18\x02 \x01(\x05\"^\n\x1aServerStreamingEchoRequest\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x15\n\rmessage_count\x18\x02 \x01(\x05\x12\x18\n\x10message_interval\x18\x03 \x01(\x05\".\n\x1bServerStreamingEchoResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"-\n\x1a\x43lientStreamingEchoRequest\x12\x0f\n\x07message\x18\x01 \x01(\t\"4\n\x1b\x43lientStreamingEchoResponse\x12\x15\n\rmessage_count\x18\x01 \x01(\x05\x32\xb0\x06\n\x0b\x45\x63hoService\x12M\n\x04\x45\x63ho\x12!.grpc.gateway.testing.EchoRequest\x1a\".grpc.gateway.testing.EchoResponse\x12T\n\tEchoAbort\x12!.grpc.gateway.testing.EchoRequest\x1a\".grpc.gateway.testing.EchoResponse\"\x00\x12@\n\x04NoOp\x12\x1b.grpc.gateway.testing.Empty\x1a\x1b.grpc.gateway.testing.Empty\x12|\n\x13ServerStreamingEcho\x12\x30.grpc.gateway.testing.ServerStreamingEchoRequest\x1a\x31.grpc.gateway.testing.ServerStreamingEchoResponse0\x01\x12\x83\x01\n\x18ServerStreamingEchoAbort\x12\x30.grpc.gateway.testing.ServerStreamingEchoRequest\x1a\x31.grpc.gateway.testing.ServerStreamingEchoResponse\"\x00\x30\x01\x12|\n\x13\x43lientStreamingEcho\x12\x30.grpc.gateway.testing.ClientStreamingEchoRequest\x1a\x31.grpc.gateway.testing.ClientStreamingEchoResponse(\x01\x12[\n\x0e\x46ullDuplexEcho\x12!.grpc.gateway.testing.EchoRequest\x1a\".grpc.gateway.testing.EchoResponse(\x01\x30\x01\x12[\n\x0eHalfDuplexEcho\x12!.grpc.gateway.testing.EchoRequest\x1a\".grpc.gateway.testing.EchoResponse(\x01\x30\x01\x62\x06proto3')



_EMPTY = DESCRIPTOR.message_types_by_name['Empty']
_ECHOREQUEST = DESCRIPTOR.message_types_by_name['EchoRequest']
_ECHORESPONSE = DESCRIPTOR.message_types_by_name['EchoResponse']
_SERVERSTREAMINGECHOREQUEST = DESCRIPTOR.message_types_by_name['ServerStreamingEchoRequest']
_SERVERSTREAMINGECHORESPONSE = DESCRIPTOR.message_types_by_name['ServerStreamingEchoResponse']
_CLIENTSTREAMINGECHOREQUEST = DESCRIPTOR.message_types_by_name['ClientStreamingEchoRequest']
_CLIENTSTREAMINGECHORESPONSE = DESCRIPTOR.message_types_by_name['ClientStreamingEchoResponse']
Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'echo_pb2'
  # @@protoc_insertion_point(class_scope:grpc.gateway.testing.Empty)
  })
_sym_db.RegisterMessage(Empty)

EchoRequest = _reflection.GeneratedProtocolMessageType('EchoRequest', (_message.Message,), {
  'DESCRIPTOR' : _ECHOREQUEST,
  '__module__' : 'echo_pb2'
  # @@protoc_insertion_point(class_scope:grpc.gateway.testing.EchoRequest)
  })
_sym_db.RegisterMessage(EchoRequest)

EchoResponse = _reflection.GeneratedProtocolMessageType('EchoResponse', (_message.Message,), {
  'DESCRIPTOR' : _ECHORESPONSE,
  '__module__' : 'echo_pb2'
  # @@protoc_insertion_point(class_scope:grpc.gateway.testing.EchoResponse)
  })
_sym_db.RegisterMessage(EchoResponse)

ServerStreamingEchoRequest = _reflection.GeneratedProtocolMessageType('ServerStreamingEchoRequest', (_message.Message,), {
  'DESCRIPTOR' : _SERVERSTREAMINGECHOREQUEST,
  '__module__' : 'echo_pb2'
  # @@protoc_insertion_point(class_scope:grpc.gateway.testing.ServerStreamingEchoRequest)
  })
_sym_db.RegisterMessage(ServerStreamingEchoRequest)

ServerStreamingEchoResponse = _reflection.GeneratedProtocolMessageType('ServerStreamingEchoResponse', (_message.Message,), {
  'DESCRIPTOR' : _SERVERSTREAMINGECHORESPONSE,
  '__module__' : 'echo_pb2'
  # @@protoc_insertion_point(class_scope:grpc.gateway.testing.ServerStreamingEchoResponse)
  })
_sym_db.RegisterMessage(ServerStreamingEchoResponse)

ClientStreamingEchoRequest = _reflection.GeneratedProtocolMessageType('ClientStreamingEchoRequest', (_message.Message,), {
  'DESCRIPTOR' : _CLIENTSTREAMINGECHOREQUEST,
  '__module__' : 'echo_pb2'
  # @@protoc_insertion_point(class_scope:grpc.gateway.testing.ClientStreamingEchoRequest)
  })
_sym_db.RegisterMessage(ClientStreamingEchoRequest)

ClientStreamingEchoResponse = _reflection.GeneratedProtocolMessageType('ClientStreamingEchoResponse', (_message.Message,), {
  'DESCRIPTOR' : _CLIENTSTREAMINGECHORESPONSE,
  '__module__' : 'echo_pb2'
  # @@protoc_insertion_point(class_scope:grpc.gateway.testing.ClientStreamingEchoResponse)
  })
_sym_db.RegisterMessage(ClientStreamingEchoResponse)

_ECHOSERVICE = DESCRIPTOR.services_by_name['EchoService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _EMPTY._serialized_start=36
  _EMPTY._serialized_end=43
  _ECHOREQUEST._serialized_start=45
  _ECHOREQUEST._serialized_end=75
  _ECHORESPONSE._serialized_start=77
  _ECHORESPONSE._serialized_end=131
  _SERVERSTREAMINGECHOREQUEST._serialized_start=133
  _SERVERSTREAMINGECHOREQUEST._serialized_end=227
  _SERVERSTREAMINGECHORESPONSE._serialized_start=229
  _SERVERSTREAMINGECHORESPONSE._serialized_end=275
  _CLIENTSTREAMINGECHOREQUEST._serialized_start=277
  _CLIENTSTREAMINGECHOREQUEST._serialized_end=322
  _CLIENTSTREAMINGECHORESPONSE._serialized_start=324
  _CLIENTSTREAMINGECHORESPONSE._serialized_end=376
  _ECHOSERVICE._serialized_start=379
  _ECHOSERVICE._serialized_end=1195
# @@protoc_insertion_point(module_scope)
