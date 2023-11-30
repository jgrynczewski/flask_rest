def add(a: int | float, b: int | float) -> int | float:
    return a + b


# number = int | float
#
#
# def add2(a: number,
#         b: number
# ) -> number:
#     return a + b


print(add(1, 2))  # 3
print(add(1.0, 2.0))  # 3.0
# print(add('1', '2'))  # 12
# print(add([1], [2]))  # [1 ,2]
print(add(True, True))  # 2


from typing import Union


number = Union[int, float]

firstname: str = "John"
lastname: str = "Doe"

password: str | None = "tajne"
# password: Union[str, None]

# from typing import Optional
# password: Optional[str]


from typing import Final
CONST: Final[int] = 5
CONST = 10

# Gradual typing
def add(a: float, b: int) -> int:
    return a + b
