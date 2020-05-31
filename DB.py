import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="Soham", passwd="Comp$er23", database="Criminals")


mycursor = mydb.cursor()




#sql_insert_query = "INSERT INTO Records (Name, ID) VALUES ('Soham',3)"
#mycursor.execute(sql_insert_query)
#mydb.commit()
#print ("Record inserted successfully into python_users table")          
#mycursor.execute("SELECT Count(*) FROM Detect Group by Name")
#result = mycursor.fetchall()
#print(result)
#for i in result:
#    print(i)

mycursor.execute("SELECT * FROM Detect")
result = mycursor.fetchall()

for i in result:
    print(i)
    
mycursor.execute("SELECT count(*) FROM Detect group by Name")
result = mycursor.fetchall()

for i in result:
    print(i)
 