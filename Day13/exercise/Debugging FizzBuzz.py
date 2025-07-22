# Target is the number up to which we count
def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 and number % 5 == 0:         # or → and
            print("FizzBuzz")
        elif number % 3 == 0:           # if → elif
            print("Fizz")
        elif number % 5 == 0:           # if → elif
            print("Buzz")
        else:
            print(number)       # print([number])

print(fizz_buzz(17))