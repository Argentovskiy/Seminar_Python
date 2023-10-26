# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes 

def isPrime(n):
    if n == 1:
         return False
    if n%2==0:
            return False
    i =3
    while i < n//i+1:
        if n%i==0:
            return False
        i+=2
    return True
    
print(isPrime(1))

def is_prime(n):
    if n < 2:
         return False
    if n%2==0:
            return False
    return prime_recursion(n,3)


def prime_recursion(n,i):
        if i > n//i:
              return True
        if n%i==0:
            return False
        return(prime_recursion(n,i+2))

print (is_prime(107))