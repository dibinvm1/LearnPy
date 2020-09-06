'''
Fibonaci Series in 3 ways
'''
#Recursive Solution

def fib_rec(n):
    if n == 0 or n == 1:
        return n
    else:
        return (fib_rec(n-1)+fib_rec(n-2))

#simple iteration
def fib_iter(n):
    a=0
    b=1
    for i in range(n):
        a,b = b,a+b
    return a

#Dynamically memoization
def fib_dyn(fn, n):
    cache = {}
    if n not in cache:
        cache[n] = fn(n)
    return cache[n]

print(fib_rec(10))
print(fib_dyn(fib_iter,10))
print(fib_iter(10))