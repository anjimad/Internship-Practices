def exponent(base,power):
    return base ** power
def square_root(num):
    return num ** 0.5
def factorial(n):
    if n<0:
        return "not defined for negative numbers"
    fact=1
    for i in range(1,n+1):
            fact *=i
    return fact
print("exponent:",exponent(2,3))
print("square root:",square_root(25))
print("factorial:",factorial(5))