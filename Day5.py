b = "okay i am gonna to explain to to tot  you ABOUT MY DETAIL!!!!!!11!!!!!"
print(len(b))
print(b.lower())
print(b.upper())
print(b.strip("!"))
print(b.capitalize())
print(b.center(123))
print(b.count("to"))


a = input("Enter Your Name : ")
d = input("Enter Date : ")
c = '''Congreculation!!! 
dear Utkarsh Singh
you are selected in JEE ADVANCED
date : 18/02/2023
thank you'''

f = c.replace("18/02/2023", d)
print("***********JEE ADVANCED RESULT**************")
print(f.replace("Utkarsh Singh", a))
