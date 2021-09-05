import ast

class IsDigit:
    def __init__(self, *, allow_floats: bool = False, allow_ints: bool = True) -> None:
        """Class constructor

        :param allow_floats: Whether or not a float should return True, defaults to False
        :type allow_floats: bool, optional
        :param allow_ints: Wether or not an int should return True, defaults to True
        :type allow_ints: bool, optional
        """
        self.allow_floats = allow_floats
        self.allow_ints = allow_ints

    def is_digit(self, item: str) -> bool:
        """Check if int or float is a digit"""
        item_type = None
        try:
            int(item)
            item_type = int
        except ValueError:
            try:
                float(item)
                item_type = float
            except ValueError:
                print('value')
                return False
        if isinstance(item_type, int):
            return self.allow_ints
        elif isinstance(item_type, float):
            return self.allow_floats
        else:
            print('final')
            return False

    def __call__(self, item: str) -> bool:
        return self.is_digit(item)

    def __repr__(self) -> str:
        return f"IsDigit(allow_floats={self.allow_floats}, allow_ints={self.allow_ints})"