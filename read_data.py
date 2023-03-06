import pymysql

#database connection
connection = pymysql.connect(host="localhost", user="root", passwd="", database="tkinterdb")
cursor = connection.cursor()

# queries for retrievint all rows
retrive = "Select * from StudentsTable;"

#executing the quires
cursor.execute(retrive)
records = cursor.fetchall()
print("***************************")
for record in records:
	print(record)
print("***************************")
print("Data Read suceesfully")

