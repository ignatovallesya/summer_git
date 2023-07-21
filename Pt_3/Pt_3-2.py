# 3.2
n = int(input("Введите число: "))
fib = lambda n, a=0, b=1: [a] + fib(n, b, a + b) if b <= n else [a]
print("Последовательность чисел Фиббоначи, не привышающих ", n, ":", fib(n))
