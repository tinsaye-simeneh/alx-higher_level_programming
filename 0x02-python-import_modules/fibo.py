B#!/usr/bin/python3
def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print(b, end=" ")
        a, b = b, a+b
    print()
