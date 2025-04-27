def penildrome(a):
    return a == a[::-1]


a = input("enter a string : ")
yoyo = penildrome(a)

if yoyo:
    print("this is pelindrome word")

else:
    print("this is not a pelindrome word")
