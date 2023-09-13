class Point:
    def __init__(self, x, y) -> None:
        self._x = x
        self._y = y

    def __str__(self) -> str:
        return f"x_{self._x}, y_{self._y}"
    
    def __eq__(self, other: object) -> bool:
        if isinstance(self, Point):
            return self._x == other._x and self._y == other._y
        return False
    
    def __add__(self, other):
        return Point(self._x + other._x, self._y + other._y)