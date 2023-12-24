from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class BankingEvent(_message.Message):
    __slots__ = ["id", "interface", "money"]
    ID_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_FIELD_NUMBER: _ClassVar[int]
    MONEY_FIELD_NUMBER: _ClassVar[int]
    id: int
    interface: str
    money: int
    def __init__(self, id: _Optional[int] = ..., interface: _Optional[str] = ..., money: _Optional[int] = ...) -> None: ...

class Response(_message.Message):
    __slots__ = ["id", "result"]
    ID_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    id: int
    result: str
    def __init__(self, id: _Optional[int] = ..., result: _Optional[str] = ...) -> None: ...

class NewBalance(_message.Message):
    __slots__ = ["updatedbalance"]
    UPDATEDBALANCE_FIELD_NUMBER: _ClassVar[int]
    updatedbalance: int
    def __init__(self, updatedbalance: _Optional[int] = ...) -> None: ...

class PropagateResp(_message.Message):
    __slots__ = ["resp"]
    RESP_FIELD_NUMBER: _ClassVar[int]
    resp: str
    def __init__(self, resp: _Optional[str] = ...) -> None: ...
