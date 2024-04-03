from typing import Dict, Sequence, Tuple

from boa3.builtin.compile_time import public


@public
def Main() -> Sequence[str]:
    a: Dict[str, int] = {'one': 1, 'two': 2, 'three': 3}
    b: Tuple[str] = a.keys()
    return b
