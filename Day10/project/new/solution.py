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
    should_accumulate = True        # 결과값 누적을 위한 true/false (true : 누적 / false : 누적안함)
    num1 = float(input("What's the first number? : "))      # num1은 while문 안에 있으면 안됨

    while should_accumulate:        # 반복되기 시작하면 사용하는 함수 : while
        for calculation_symbol in operations:
            print(calculation_symbol)

        symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number? : "))
        
        # print(operations["-"](3, 1)) ← 이걸 참고로 작성
        cal_value = operations[symbol](num1,num2)

        print(f"{num1} {symbol} {num2} = {cal_value}")

        qustion = input(f"Type 'y' to continue calculation with {cal_value}, or type 'n' to start a new calculation : ")

        if qustion == "y":
            num1 = cal_value
        else:
            should_accumulate = False
            print("\n" * 30)
            calculation()


calculation()



