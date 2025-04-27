def callon (b=20,a=10):

    b=b+a

    

    a=b-a

    print(b, "#",a)

    

    return b

x=100

y=200

x=callon (x,y)

print(x,"@",y)

y=callon (y)

print(x,"@",y)


