from typing import Callable


def add(n1: float, n2: float) -> float:
    return n1 + n2


def subtract(n1: float, n2: float) -> float:
    return n1 - n2


def multiply(n1: float, n2: float) -> float:
    return n1 * n2


def divide(n1: float, n2: float) -> float:
    if n2 == 0:
        raise Exception("Can't divide by 0")
    return n1 / n2


operations: dict[str, Callable[[float, float], float]] = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator()->None:
    while True:  # Outer loop for restarting calculator
        should_accumulate: bool = True

        # Get first number with validation
        while True:
            try:
                num1: float = float(input("What is the first number?: "))
                break
            except ValueError:
                print("Please enter a valid number.")

        while should_accumulate:
            print("\n".join(operations.keys()))
            operation: str = input("Pick an operation: ")

            # Validate operation
            if operation not in operations:
                print(f"Invalid operation. Choose from: {', '.join(operations.keys())}")
                continue

            # Get second number with validation
            while True:
                try:
                    num2: float = float(input("What is the second number?: "))
                    break
                except ValueError:
                    print("Please enter a valid number.")

            try:
                answer: float = operations[operation](num1, num2)
                print(f"{num1} {operation} {num2} = {answer}")
            except Exception as e:
                print(f"Error: {e}")
                continue

            choice: str = input(
                f"Type y to continue calculating with {answer} or type n to start with new numbers: "
            )
            if choice == "y":
                num1 = answer
            else:
                should_accumulate = False
                print('\n'*20)
                break  # Exit inner loop to restart

if __name__ == "__main__":
    calculator()    

