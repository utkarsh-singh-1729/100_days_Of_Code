# factorial
# factorial(3)=3*2*1
# factorial(4)=4*3*2*1

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))

# febonacci sequence
# f(0)=0
# f(1)=1
# f(n)= f(n-1)+f(n-2)
def febonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return (n-1)+(n-2)
print(febonacci(5))



