from boa3.builtin.compile_time import public
from boa3.builtin.type import UInt160


@public
def uint160(arg: bytes) -> bytes:
    return UInt160(arg)