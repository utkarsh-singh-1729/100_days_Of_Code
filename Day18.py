import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", user="root", password="vin07@SIN", database="mycompany"
)

mycursor = mydb.cursor()
# i = int(input("enter your company id :"))
# f = input("enter your first name :")
# l = input("enter your last name :")
# e = input("enter your email :")
# m = input("enter your mobile no. :")

mycursor.execute("INSERT INTO employ(id, First_Name, Last_Name, Email, Mobile) VALUES(13444,'jfdjshg','jfdjsdhg','jfdjshgd',787685768754)")


# mycursor.execute(sql, val)

mydb.commit();

print("Voila! database update sucessfully")