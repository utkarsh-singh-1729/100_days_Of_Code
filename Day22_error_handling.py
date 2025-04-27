n= input("enter a number :")
try:

    def factorial(n):
        if n==0 or n==1:
            return 1
        else:
            return n*factorial(n-1)
    print(factorial(n))
except Exception as e:
    print(e)