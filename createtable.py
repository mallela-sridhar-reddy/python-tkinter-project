import pymysql

#database connection
connection = pymysql.connect(host="localhost", user="root", passwd="", database="tkinterdb")
cursor = connection.cursor()
# Query for creating table
StudentsTableSql = """CREATE TABLE StudentsTable(
Date CHAR(20),
Name CHAR(50) PRIMARY KEY,
Mobile_No  CHAR(20),
Alternate_No CHAR(20),
Email_Id CHAR(50),
Address CHAR(20),
Course_Intended CHAR(20),
Batch_Preffered CHAR(20),
How_You_Come_To_Know_Us CHAR(20),
Are_You_Experienced_Or_Fresher CHAR(20),
Contact_Person_From_Besant CHAR(50),
Counselor CHAR(50),
Fees CHAR(10),
Comment CHAR(150))"""
cursor.execute(StudentsTableSql)
print("Table created Successfully")
connection.close()

