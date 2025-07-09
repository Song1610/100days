# 에러가 있을 수 있음

def is_prime(num):
    for i in range(2,num+1):
        prime_value = num % i
        
        if i == num and prime_value == 0:
            return True # 소수
        elif num == 2 or num == 3 or num == 5:
            return True
        elif i == 2 and prime_value == 0:
            return False    # 소수 아님
        elif i == 3 and prime_value == 0:
            return False
        

print(is_prime(73))
print(is_prime(75))
print(is_prime(2))
print(is_prime(14))

