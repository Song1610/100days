# calculator project
import Day10.project.old.art as art

def add(n1, n2):
    return n1 + n2

# Todo 1
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

# Todo 2
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# Todo 3: 사전 연산을 사용하여 계산을 수행합니다. 사전을 사용하여 4 * 8을 곱합니다.
# print(operations["*"](4,8))

def calculator():
    print(art.logo)
    accumulate = True
    num1 = float(input("first number : "))

    while accumulate:
        for symbol in operations:
            print(symbol)
        op = input("등호 선택: ")
        num2 = float(input("second number : "))

        result = operations[op](num1,num2)
        print(f"{num1} {op} {num2} = {result}")

        choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        if choice == "y":
            num1 = result
        else:
            accumulate = False
            print("\n" * 5)
            calculator()

calculator()