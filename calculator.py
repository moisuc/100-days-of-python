from typing import Callable, Dict

def add(n1: float, n2: float) -> float:
    return n1 + n2


def substract(n1: float, n2: float) -> float:
    return n1 - n2


def multiply(n1: float, n2: float) -> float:
    return n1 * n2



def divide(n1: float, n2: float) -> float:
    if n2 == 0:
        raise Exception("Can't divide by 0")
    return n1 / n2

operations: Dict[str, Callable[[float, float], float]] = {
    '+':add,
    '-':substract,
    '*':multiply,
    '/':divide
}

print(operations['*'](4,8))