from flask import Flask,request,render_template
from flaskext.mysql import MySQL
mysql=MySQL()

app=Flask(__name__)
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']='vin07@SIN'
app.config['MYSQL_DATABASE_DB']='mycompany'
app.config['MYSQL_DATABASE_host']='127.0.0.1:3306'
mysql.init_app(app)

@app.route('/',methods=['POST'])
def get_data():
 return render_template("sample.html")
 
 if request.method=='POST':
    first_name=request.form['fname']
    last_name=request.form['lname']
    emailid=request.form['emailid']
    connection = mysql.get_db()
    cursor = connection.cursor()
 query="INSERT INTO nam(f_name,l_name,e_id) VALUES(%s,%s,%s)"
 cursor.execute(query,(first_name,last_name,email_id))

connection.commit()
return "nothing fucked"
#  else:
#     return("something fucked up")

if __name__=='__main__':
app.run(debug=True)














