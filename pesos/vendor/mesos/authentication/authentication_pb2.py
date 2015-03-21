# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mesos/authentication/authentication.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ... import mesos


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mesos/authentication/authentication.proto',
  package='mesos.internal',
  serialized_pb=_b('\n)mesos/authentication/authentication.proto\x12\x0emesos.internal\x1a\x11mesos/mesos.proto\"\"\n\x13\x41uthenticateMessage\x12\x0b\n\x03pid\x18\x01 \x02(\t\"5\n\x1f\x41uthenticationMechanismsMessage\x12\x12\n\nmechanisms\x18\x01 \x03(\t\"=\n\x1a\x41uthenticationStartMessage\x12\x11\n\tmechanism\x18\x01 \x02(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\")\n\x19\x41uthenticationStepMessage\x12\x0c\n\x04\x64\x61ta\x18\x01 \x02(\x0c\" \n\x1e\x41uthenticationCompletedMessage\"\x1d\n\x1b\x41uthenticationFailedMessage\"+\n\x1a\x41uthenticationErrorMessage\x12\r\n\x05\x65rror\x18\x01 \x01(\tB\x1a\n\x10org.apache.mesosB\x06Protos')
  ,
  dependencies=[mesos.mesos_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_AUTHENTICATEMESSAGE = _descriptor.Descriptor(
  name='AuthenticateMessage',
  full_name='mesos.internal.AuthenticateMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pid', full_name='mesos.internal.AuthenticateMessage.pid', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=80,
  serialized_end=114,
)


_AUTHENTICATIONMECHANISMSMESSAGE = _descriptor.Descriptor(
  name='AuthenticationMechanismsMessage',
  full_name='mesos.internal.AuthenticationMechanismsMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mechanisms', full_name='mesos.internal.AuthenticationMechanismsMessage.mechanisms', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=116,
  serialized_end=169,
)


_AUTHENTICATIONSTARTMESSAGE = _descriptor.Descriptor(
  name='AuthenticationStartMessage',
  full_name='mesos.internal.AuthenticationStartMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mechanism', full_name='mesos.internal.AuthenticationStartMessage.mechanism', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='mesos.internal.AuthenticationStartMessage.data', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=171,
  serialized_end=232,
)


_AUTHENTICATIONSTEPMESSAGE = _descriptor.Descriptor(
  name='AuthenticationStepMessage',
  full_name='mesos.internal.AuthenticationStepMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='mesos.internal.AuthenticationStepMessage.data', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=234,
  serialized_end=275,
)


_AUTHENTICATIONCOMPLETEDMESSAGE = _descriptor.Descriptor(
  name='AuthenticationCompletedMessage',
  full_name='mesos.internal.AuthenticationCompletedMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=277,
  serialized_end=309,
)


_AUTHENTICATIONFAILEDMESSAGE = _descriptor.Descriptor(
  name='AuthenticationFailedMessage',
  full_name='mesos.internal.AuthenticationFailedMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=311,
  serialized_end=340,
)


_AUTHENTICATIONERRORMESSAGE = _descriptor.Descriptor(
  name='AuthenticationErrorMessage',
  full_name='mesos.internal.AuthenticationErrorMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='error', full_name='mesos.internal.AuthenticationErrorMessage.error', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=342,
  serialized_end=385,
)

DESCRIPTOR.message_types_by_name['AuthenticateMessage'] = _AUTHENTICATEMESSAGE
DESCRIPTOR.message_types_by_name['AuthenticationMechanismsMessage'] = _AUTHENTICATIONMECHANISMSMESSAGE
DESCRIPTOR.message_types_by_name['AuthenticationStartMessage'] = _AUTHENTICATIONSTARTMESSAGE
DESCRIPTOR.message_types_by_name['AuthenticationStepMessage'] = _AUTHENTICATIONSTEPMESSAGE
DESCRIPTOR.message_types_by_name['AuthenticationCompletedMessage'] = _AUTHENTICATIONCOMPLETEDMESSAGE
DESCRIPTOR.message_types_by_name['AuthenticationFailedMessage'] = _AUTHENTICATIONFAILEDMESSAGE
DESCRIPTOR.message_types_by_name['AuthenticationErrorMessage'] = _AUTHENTICATIONERRORMESSAGE

AuthenticateMessage = _reflection.GeneratedProtocolMessageType('AuthenticateMessage', (_message.Message,), dict(
  DESCRIPTOR = _AUTHENTICATEMESSAGE,
  __module__ = 'mesos.authentication.authentication_pb2'
  # @@protoc_insertion_point(class_scope:mesos.internal.AuthenticateMessage)
  ))
_sym_db.RegisterMessage(AuthenticateMessage)

AuthenticationMechanismsMessage = _reflection.GeneratedProtocolMessageType('AuthenticationMechanismsMessage', (_message.Message,), dict(
  DESCRIPTOR = _AUTHENTICATIONMECHANISMSMESSAGE,
  __module__ = 'mesos.authentication.authentication_pb2'
  # @@protoc_insertion_point(class_scope:mesos.internal.AuthenticationMechanismsMessage)
  ))
_sym_db.RegisterMessage(AuthenticationMechanismsMessage)

AuthenticationStartMessage = _reflection.GeneratedProtocolMessageType('AuthenticationStartMessage', (_message.Message,), dict(
  DESCRIPTOR = _AUTHENTICATIONSTARTMESSAGE,
  __module__ = 'mesos.authentication.authentication_pb2'
  # @@protoc_insertion_point(class_scope:mesos.internal.AuthenticationStartMessage)
  ))
_sym_db.RegisterMessage(AuthenticationStartMessage)

AuthenticationStepMessage = _reflection.GeneratedProtocolMessageType('AuthenticationStepMessage', (_message.Message,), dict(
  DESCRIPTOR = _AUTHENTICATIONSTEPMESSAGE,
  __module__ = 'mesos.authentication.authentication_pb2'
  # @@protoc_insertion_point(class_scope:mesos.internal.AuthenticationStepMessage)
  ))
_sym_db.RegisterMessage(AuthenticationStepMessage)

AuthenticationCompletedMessage = _reflection.GeneratedProtocolMessageType('AuthenticationCompletedMessage', (_message.Message,), dict(
  DESCRIPTOR = _AUTHENTICATIONCOMPLETEDMESSAGE,
  __module__ = 'mesos.authentication.authentication_pb2'
  # @@protoc_insertion_point(class_scope:mesos.internal.AuthenticationCompletedMessage)
  ))
_sym_db.RegisterMessage(AuthenticationCompletedMessage)

AuthenticationFailedMessage = _reflection.GeneratedProtocolMessageType('AuthenticationFailedMessage', (_message.Message,), dict(
  DESCRIPTOR = _AUTHENTICATIONFAILEDMESSAGE,
  __module__ = 'mesos.authentication.authentication_pb2'
  # @@protoc_insertion_point(class_scope:mesos.internal.AuthenticationFailedMessage)
  ))
_sym_db.RegisterMessage(AuthenticationFailedMessage)

AuthenticationErrorMessage = _reflection.GeneratedProtocolMessageType('AuthenticationErrorMessage', (_message.Message,), dict(
  DESCRIPTOR = _AUTHENTICATIONERRORMESSAGE,
  __module__ = 'mesos.authentication.authentication_pb2'
  # @@protoc_insertion_point(class_scope:mesos.internal.AuthenticationErrorMessage)
  ))
_sym_db.RegisterMessage(AuthenticationErrorMessage)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\020org.apache.mesosB\006Protos'))
# @@protoc_insertion_point(module_scope)