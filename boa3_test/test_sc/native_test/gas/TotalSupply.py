from boa3.builtin.compile_time import public
from boa3.builtin.nativecontract.gas import GAS


@public
def main() -> int:
    return GAS.totalSupply()
