import mysql.connector
import face_recognition
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='root@123',
    port='3306',
    database='demo'
)
mycursor=mydb.cursor()
mycursor.execute("""SELECT * FROM `criminal_record` WHERE `name`='{}'""".format(name))
user=mycursor.fetchone()
print(mycursor.fetchone())
mycursor.execute("SELECT * FROM criminal_record")
result = mycursor.fetchall()

for i in result:
    print(i)

mycursor.execute("SELECT count(*) FROM criminal_record group by name")
results = mycursor.fetchall()
for i in results:
    print(i)
if user==None:
    print("no record")
else:
    print(user[1])
    print(user[2])
    print(user[3])
    print(user[4])
    print(user[5])

