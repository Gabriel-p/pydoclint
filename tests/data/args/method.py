class MyClass:
    def __init__(self):
        pass

    def func1_1(self, arg1: int, arg2: float) -> None:
        pass

    def func1_2(self, arg1: int, arg2: float) -> None:
        """"""
        pass

    def func1_3(self, arg1: str, arg2: list[int]) -> bool:
        """Something

        Returns
        -------
        bool
            Something else
        """
        return True

    def func1_4(self) -> bool:
        return False

    def func1_5(self) -> None:
        """Something

        Returns
        -------
        None
        """
        return None

    def func1_6(self) -> None:
        """
        Something

        Parameters
        ----------
        arg1 : int
            Arg 1

        Returns
        -------
        None
        """
        return None

    def func2(self, arg1: int, arg2: float | int | None) -> int | list[float]:
        """
        Do something.

        Parameters
        ----------
        arg1 : int
            Arg 1

        Returns
        -------
        int :
            Result
        """
        return 1

    def func3(self, arg1: int, arg2: float) -> int:
        """
        Do something.

        Parameters
        ----------
        arg1 : int
            Arg 1
        arg2 : float
            Arg 2
        arg3 : Optional[Union[float, int, str]]
            Arg 3

        Returns
        -------
        int :
            Result
        """
        return 1

    async def func4(self, arg1: int, arg2: float) -> int:
        """
        Do something.

        Parameters
        ----------
        arg2 : float
            Arg 2
        arg1 : int
            Arg 1

        Returns
        -------
        int :
            Result
        """
        return 1

    def func5(self, arg1: int, arg2: float) -> int:
        """
        Do something.

        Parameters
        ----------
        arg1 : list[str]
            Arg 1
        arg2 : str
            Arg 2

        Returns
        -------
        int :
            Result
        """
        return 1

    def func6(self, arg1: int, arg2: float) -> int:
        """
        Do something.

        Parameters
        ----------
        arg2 : str
            Arg 2
        arg1 : list[str]
            Arg 1

        Returns
        -------
        int :
            Result
        """
        return 1

    def func7(self, arg1: int, arg2: float) -> int:
        """
        Do something.

        Parameters
        ----------
        arg1 : int
            Arg 1
        arg2 : float
            Arg 2

        Returns
        -------
        int :
            Result
        """

        def func72(arg3: list, arg4: tuple, arg5: dict) -> None:
            """
            Do something else

            arg100: int
                Some arg

            Returns
            -------
            None
            """
            return None

        return 2