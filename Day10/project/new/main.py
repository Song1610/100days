# 내가 작성한 부분까지
import art

def add(n1, n2):
    return n1 + n2

# Todo 1: 다른 3가지 function 작성(subtract(-), multiply(*), divide(/))
def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# Todo 2 : 위의 4개의 함수를 사전에 값으로 추가
operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

# Todo 3 : 사전 작업을 사용하여 계산을 수행
def calculation():
    print(art.logo)
    num1 = float(input("What's the first number? : "))

    oper = input(" +\n -\n *\n /\nPick an operation: ")
    num2 = float(input("What's the next number? : "))
    cal_value = operations[oper](num1,num2)

    print(f"{num1} {oper} {num2} = {cal_value}")

    qustion = input(f"Type 'y' to continue calculation with {cal_value}, or type 'n' to start a nuw calculation : ")

    if qustion == "y":
        num1 = cal_value
        oper = input(" +\n -\n *\n /\nPick an operation: ")
        num2 = float(input("What's the next number? : "))
        cal_value = operations[oper](num1, num2)

        print(f"{num1} {oper} {num2} = {cal_value}")

    else:
        print("끝")

calculation()

# print(operations["-"](3, 1))

