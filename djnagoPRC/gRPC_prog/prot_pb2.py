# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: prot.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nprot.proto\"4\n\nDataServer\x12\n\n\x02ip\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\t\x12\x0c\n\x04mode\x18\x03 \x01(\t\"\x1f\n\tDataChunk\x12\x12\n\ndata_chunk\x18\x01 \x01(\t\"\x07\n\x05\x45mpty\"y\n\nDataClient\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x11\n\tip_status\x18\x02 \x01(\t\x12\x11\n\tprotocols\x18\x03 \x01(\t\x12\x12\n\nopen_ports\x18\x04 \x01(\t\x12\r\n\x05state\x18\x05 \x01(\t\x12\x11\n\tid_client\x18\x06 \x01(\t2F\n\x03RPC\x12 \n\x04scan\x12\x0b.DataClient\x1a\x0b.DataServer\x12\x1d\n\x05\x63hunk\x12\n.DataChunk\x1a\x06.Empty(\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'prot_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _DATASERVER._serialized_start=14
  _DATASERVER._serialized_end=66
  _DATACHUNK._serialized_start=68
  _DATACHUNK._serialized_end=99
  _EMPTY._serialized_start=101
  _EMPTY._serialized_end=108
  _DATACLIENT._serialized_start=110
  _DATACLIENT._serialized_end=231
  _RPC._serialized_start=233
  _RPC._serialized_end=303
# @@protoc_insertion_point(module_scope)
