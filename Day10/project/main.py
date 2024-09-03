# calculator project
import art
print(art.logo)

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
operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


result = operation["*"](n1 = 4, n2 = 8)
print(result)