def fibonacci(n):
    fib=[0,1]
    for i in range(2,n):
        fib.append(fib[i-1]+fib[i-2])
    return fib
n=int(input("Enter Number"))
result=fibonacci(n)
print("Fibonacci series for",n,":",result)

# Enter Number7
# Fibonacci series for 7 : [0, 1, 1, 2, 3, 5, 8]
