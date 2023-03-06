import pymysql

#database connection
connection = pymysql.connect(host="localhost", user="root", passwd="", database="tkinterdb")
cursor = connection.cursor()

updateSql = "TRUNCATE TABLE StudentsTable;"
cursor.execute(updateSql)


#commiting the connection then closing it.
connection.commit()
print("Data Updated Successfully in Database")
connection.close()

