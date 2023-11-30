# Funckje

def div(a: float, b: float) -> float | Exception:
    return a / b


def div2(a: float, b: float) -> float | ZeroDivisionError:
    return a / b


print(div2.__annotations__)


from typing import Callable


def fetch(url: str,
          on_sucess: Callable,
          on_error: Callable
) -> None:
    ...


