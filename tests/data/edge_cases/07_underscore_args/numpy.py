# From issue: https://github.com/jsh9/pydoclint/issues/87
def foo(_: int, __: str, __a: dict, b: float, ___: bool):
    """Bar.

    Parameters
    ----------
    __a : dict
        a dict
    b : float
        a number
    """
    pass
