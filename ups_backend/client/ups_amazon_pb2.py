# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ups_amazon.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import world_amazon_pb2 as world__amazon__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ups_amazon.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x10ups_amazon.proto\x1a\x12world_amazon.proto\"\xa7\x01\n\tAReqTruck\x12\"\n\twarehouse\x18\x01 \x02(\x0b\x32\x0f.AInitWarehouse\x12\x1a\n\x07product\x18\x02 \x03(\x0b\x32\t.AProduct\x12\x11\n\tpackageid\x18\x03 \x02(\x03\x12\x0f\n\x07\x62uyer_x\x18\x04 \x02(\x05\x12\x0f\n\x07\x62uyer_y\x18\x05 \x02(\x05\x12\x10\n\x08ups_name\x18\x06 \x01(\t\x12\x13\n\x0bsequenceNum\x18\x07 \x02(\x03\"K\n\x10\x41\x43ompleteLoading\x12\x0f\n\x07truckid\x18\x01 \x02(\x05\x12\x11\n\tpackageid\x18\x02 \x02(\x03\x12\x13\n\x0bsequenceNum\x18\x03 \x02(\x03\"r\n\x05\x41Msgs\x12\x1c\n\x08reqtruck\x18\x01 \x03(\x0b\x32\n.AReqTruck\x12*\n\x0f\x63ompleteloading\x18\x02 \x03(\x0b\x32\x11.ACompleteLoading\x12\x0c\n\x04\x61\x63ks\x18\x03 \x03(\x03\x12\x11\n\x03\x65rr\x18\x04 \x03(\x0b\x32\x04.Err\"8\n\x03\x45rr\x12\x0b\n\x03\x65rr\x18\x01 \x02(\t\x12\x14\n\x0coriginseqnum\x18\x02 \x02(\x03\x12\x0e\n\x06seqnum\x18\x03 \x02(\x03\"C\n\rUTruckArrived\x12\x0f\n\x07truckid\x18\x01 \x02(\x05\x12\x11\n\tpackageid\x18\x02 \x02(\x03\x12\x0e\n\x06seqnum\x18\x03 \x02(\x03\"4\n\x0fUFinishDelivery\x12\x11\n\tpackageid\x18\x01 \x02(\x03\x12\x0e\n\x06seqnum\x18\x02 \x02(\x03\"j\n\x05UMsgs\x12\x1e\n\x06trucks\x18\x01 \x03(\x0b\x32\x0e.UTruckArrived\x12 \n\x06\x66inish\x18\x02 \x03(\x0b\x32\x10.UFinishDelivery\x12\x0c\n\x04\x61\x63ks\x18\x03 \x03(\x03\x12\x11\n\x03\x65rr\x18\x04 \x03(\x0b\x32\x04.Err')
  ,
  dependencies=[world__amazon__pb2.DESCRIPTOR,])




_AREQTRUCK = _descriptor.Descriptor(
  name='AReqTruck',
  full_name='AReqTruck',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='warehouse', full_name='AReqTruck.warehouse', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='product', full_name='AReqTruck.product', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='packageid', full_name='AReqTruck.packageid', index=2,
      number=3, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='buyer_x', full_name='AReqTruck.buyer_x', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='buyer_y', full_name='AReqTruck.buyer_y', index=4,
      number=5, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ups_name', full_name='AReqTruck.ups_name', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sequenceNum', full_name='AReqTruck.sequenceNum', index=6,
      number=7, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=41,
  serialized_end=208,
)


_ACOMPLETELOADING = _descriptor.Descriptor(
  name='ACompleteLoading',
  full_name='ACompleteLoading',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='truckid', full_name='ACompleteLoading.truckid', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='packageid', full_name='ACompleteLoading.packageid', index=1,
      number=2, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sequenceNum', full_name='ACompleteLoading.sequenceNum', index=2,
      number=3, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=210,
  serialized_end=285,
)


_AMSGS = _descriptor.Descriptor(
  name='AMsgs',
  full_name='AMsgs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='reqtruck', full_name='AMsgs.reqtruck', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='completeloading', full_name='AMsgs.completeloading', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='acks', full_name='AMsgs.acks', index=2,
      number=3, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='err', full_name='AMsgs.err', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=287,
  serialized_end=401,
)


_ERR = _descriptor.Descriptor(
  name='Err',
  full_name='Err',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='err', full_name='Err.err', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='originseqnum', full_name='Err.originseqnum', index=1,
      number=2, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='seqnum', full_name='Err.seqnum', index=2,
      number=3, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=403,
  serialized_end=459,
)


_UTRUCKARRIVED = _descriptor.Descriptor(
  name='UTruckArrived',
  full_name='UTruckArrived',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='truckid', full_name='UTruckArrived.truckid', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='packageid', full_name='UTruckArrived.packageid', index=1,
      number=2, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='seqnum', full_name='UTruckArrived.seqnum', index=2,
      number=3, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=461,
  serialized_end=528,
)


_UFINISHDELIVERY = _descriptor.Descriptor(
  name='UFinishDelivery',
  full_name='UFinishDelivery',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='packageid', full_name='UFinishDelivery.packageid', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='seqnum', full_name='UFinishDelivery.seqnum', index=1,
      number=2, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=530,
  serialized_end=582,
)


_UMSGS = _descriptor.Descriptor(
  name='UMsgs',
  full_name='UMsgs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='trucks', full_name='UMsgs.trucks', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='finish', full_name='UMsgs.finish', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='acks', full_name='UMsgs.acks', index=2,
      number=3, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='err', full_name='UMsgs.err', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=584,
  serialized_end=690,
)

_AREQTRUCK.fields_by_name['warehouse'].message_type = world__amazon__pb2._AINITWAREHOUSE
_AREQTRUCK.fields_by_name['product'].message_type = world__amazon__pb2._APRODUCT
_AMSGS.fields_by_name['reqtruck'].message_type = _AREQTRUCK
_AMSGS.fields_by_name['completeloading'].message_type = _ACOMPLETELOADING
_AMSGS.fields_by_name['err'].message_type = _ERR
_UMSGS.fields_by_name['trucks'].message_type = _UTRUCKARRIVED
_UMSGS.fields_by_name['finish'].message_type = _UFINISHDELIVERY
_UMSGS.fields_by_name['err'].message_type = _ERR
DESCRIPTOR.message_types_by_name['AReqTruck'] = _AREQTRUCK
DESCRIPTOR.message_types_by_name['ACompleteLoading'] = _ACOMPLETELOADING
DESCRIPTOR.message_types_by_name['AMsgs'] = _AMSGS
DESCRIPTOR.message_types_by_name['Err'] = _ERR
DESCRIPTOR.message_types_by_name['UTruckArrived'] = _UTRUCKARRIVED
DESCRIPTOR.message_types_by_name['UFinishDelivery'] = _UFINISHDELIVERY
DESCRIPTOR.message_types_by_name['UMsgs'] = _UMSGS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AReqTruck = _reflection.GeneratedProtocolMessageType('AReqTruck', (_message.Message,), dict(
  DESCRIPTOR = _AREQTRUCK,
  __module__ = 'ups_amazon_pb2'
  # @@protoc_insertion_point(class_scope:AReqTruck)
  ))
_sym_db.RegisterMessage(AReqTruck)

ACompleteLoading = _reflection.GeneratedProtocolMessageType('ACompleteLoading', (_message.Message,), dict(
  DESCRIPTOR = _ACOMPLETELOADING,
  __module__ = 'ups_amazon_pb2'
  # @@protoc_insertion_point(class_scope:ACompleteLoading)
  ))
_sym_db.RegisterMessage(ACompleteLoading)

AMsgs = _reflection.GeneratedProtocolMessageType('AMsgs', (_message.Message,), dict(
  DESCRIPTOR = _AMSGS,
  __module__ = 'ups_amazon_pb2'
  # @@protoc_insertion_point(class_scope:AMsgs)
  ))
_sym_db.RegisterMessage(AMsgs)

Err = _reflection.GeneratedProtocolMessageType('Err', (_message.Message,), dict(
  DESCRIPTOR = _ERR,
  __module__ = 'ups_amazon_pb2'
  # @@protoc_insertion_point(class_scope:Err)
  ))
_sym_db.RegisterMessage(Err)

UTruckArrived = _reflection.GeneratedProtocolMessageType('UTruckArrived', (_message.Message,), dict(
  DESCRIPTOR = _UTRUCKARRIVED,
  __module__ = 'ups_amazon_pb2'
  # @@protoc_insertion_point(class_scope:UTruckArrived)
  ))
_sym_db.RegisterMessage(UTruckArrived)

UFinishDelivery = _reflection.GeneratedProtocolMessageType('UFinishDelivery', (_message.Message,), dict(
  DESCRIPTOR = _UFINISHDELIVERY,
  __module__ = 'ups_amazon_pb2'
  # @@protoc_insertion_point(class_scope:UFinishDelivery)
  ))
_sym_db.RegisterMessage(UFinishDelivery)

UMsgs = _reflection.GeneratedProtocolMessageType('UMsgs', (_message.Message,), dict(
  DESCRIPTOR = _UMSGS,
  __module__ = 'ups_amazon_pb2'
  # @@protoc_insertion_point(class_scope:UMsgs)
  ))
_sym_db.RegisterMessage(UMsgs)


# @@protoc_insertion_point(module_scope)
