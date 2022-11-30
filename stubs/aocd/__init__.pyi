from typing import Any

def submit(
    answer: str,
    part: str = None,
    day: int = None,
    year: int = None,
    session: Any = None,
    reopen: bool = True,
    quiet: bool = False,
) -> Any: ...
def get_data(
    session: Any = None, day: int = None, year: int = None, block: bool = False
) -> str: ...
