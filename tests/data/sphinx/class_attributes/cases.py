class MyClass1:
    """
    A class that holds some things.

    .. attribute :: name
        :type: str | bool | None

        The name

    .. attribute :: indices
        :type: pd.DataFrame

        The indices

    :param arg1: The information
    :type arg1: float
    """

    name: str | bool | None
    index: pd.DataFrame

    hello: int = 1
    world: dict

    def __init__(self, arg1: int) -> None:
        self.arg1 = arg1

    def do_something(self, arg2: bool) -> int:
        """
        Do something.

        :param arg2: Arg 2
        :type arg2: str
        :return: Result
        :rtype: int
        """
        return 2


class MyClass2:
    """
    A class that holds some things.

    In this class, the class attributes and the instance attribute (self.arg1)
    are mixed together as attributes.

    .. attribute :: name
        :type: str | bool | None

        The name

    .. attribute :: indices
        :type: int

        The indices

    .. attribute :: arg1
        :type: float

        The information
    """

    name: str
    index: int

    hello: int = 1
    world: dict

    def __init__(self, arg1: int) -> None:
        self.arg1 = arg1

    def do_something(self, arg2: bool) -> int:
        """
        Do something.

        :param arg2: Arg 2
        :type arg2: str
        :return: Result
        :rtype: int
        """
        return 2


class MyClass3:
    """
    A class that holds some things.

    In this class, the class attributes and the instance attribute (self.arg1)
    are mixed together as parameters.

    :param name: The name
    :type name: str
    :param indices: The indices
    :type indices: int
    :param arg1: The information
    :type arg1: float
    """

    name: str
    index: int

    hello: int = 1
    world: dict

    def __init__(self, arg1: int) -> None:
        self.arg1 = arg1

    def do_something(self, arg2: bool) -> int:
        """
        Do something.

        :param arg2: Arg 2
        :type arg2: str
        :return: Result
        :rtype: int
        """
        return 2


class MyClass4:
    """
    This is a class

    .. attribute :: name
        :type: str

        My name
    """

    def __int__(self):
        pass


@dataclass
class MyClass5:
    """
    This is a class
    """

    morning: str
