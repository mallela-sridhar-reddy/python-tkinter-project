import pymysql

#database connection
connection = pymysql.connect(host="localhost", user="root", passwd="", database="tkinterdb")
cursor = connection.cursor()


deleteSql = "DELETE FROM Besant WHERE Name = 'sridhar'; "
cursor.execute(deleteSql )


#commiting the connection then closing it.
connection.commit()
print("Deleted Record successfully")
connection.close()
