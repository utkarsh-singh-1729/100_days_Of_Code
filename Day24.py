# DATA STRUCTURE IMPLEMENTATION
s = []
top = None
def isempty(stk):
    if(stk==[]):
        return True
        print("stack is empty")
    else:
        print("stack is not empty")
        return False

def push(stk,item):
    stk.append(item)
    top=len(stk)-1

def s_pop(stk):
    if(isempty(stk)):
        return('underflow')
    else:
        i=stk.pop()
        if(len(stk)==0):
            top = None
        else:
            top=top-1
    return i

def peek(stk):
    if(isempty(stk)):
        return('underflow')
    else:
        top=len(stk)-1
        return stk[top]

def display(stk):
    if(isempty(stk)):
        print('stack is empty')
    else:
        top=len(stk)-1
        print(stk[top],'<-----top')
        for i in range(top-1,-1,-1):
            print(stk[i])
        

while True:
    print('1. push')      
    print('2. pop')
    print('3. peek')
    print('4. Display')
    print('5. exit')

    ch =int(input("enter your choice(1-5) :"))

    if(ch==1):
        item=int(input("enter item :"))  
        push(s,item) 
        print(f'{item} added sucessfully')
        input("press any key to continue :")
    if(ch==2):
        item=s_pop(s)
        if(item=='underflow'):
            print('underflow! stack is empty')
        else:
            print(f'{item} popped sucessfully')
        input("press any key to continue :")
        
    if(ch==3):
        item=peek(s)
        if(item=='underflow'):
            print('underflow! stack is empty')
        else:
            print(f'{item} at the top')
        input("press any key to continue :")        
    if(ch==4):
        display(s)
        input("press any key to continue :")                
    if(ch==5): 
        break   