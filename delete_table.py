import pymysql

#database connection
connection = pymysql.connect(host="localhost", user="root", passwd="", database="tkinterdb")
cursor = connection.cursor()


dropSql = "DROP TABLE IF EXISTS StudentsTable;"
cursor.execute(dropSql)

#commiting the connection then closing it.
connection.commit()
print("Table Has been Deleted Successfully")
connection.close()
