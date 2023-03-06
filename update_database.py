import pymysql

#database connection
connection = pymysql.connect(host="localhost", user="root", passwd="", database="Employee")
cursor = connection.cursor()

updateSql = "UPDATE  Besant  SET NAME= 'Manasvi',EMPID=1005  WHERE ID = '2' ;"
cursor.execute(updateSql)


#commiting the connection then closing it.
connection.commit()
print("Data Updated Successfully in Database")
connection.close()

