import json
import pyodbc

# List the available ODBC drivers & Pick a compatible driver
# drivers = [driver for driver in pyodbc.drivers()]
# for driver in drivers:
#     print(driver)

# Create a new connection
conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};Server={server};Database={database};UID={user};PWD={password};')
cursor = conn.cursor()

# CREATE TABLE
cursor.execute("""
    IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'People')
    CREATE TABLE People (
        ID INT PRIMARY KEY IDENTITY(1,1),
        Name NVARCHAR(100),
        Age INT
    )
""")
conn.commit()

# CREATE - Insert a new record
cursor.execute("INSERT INTO People (Name, Age) VALUES (?, ?)", ('John Doe', 30))
conn.commit()

# READ - Select records
cursor.execute("SELECT * FROM People")
for row in cursor:
    print(row)

# UPDATE - Update a record
cursor.execute("UPDATE People SET Age = ? WHERE Name = ?", (31, 'John Doe'))
conn.commit()

# READ - Select 1 record
cursor.execute("SELECT * FROM People")
row = cursor.fetchone()
while row:
    print(row)
    row = cursor.fetchone()

# DELETE - Delete a record
cursor.execute("DELETE FROM People WHERE Name = ?", ('John Doe',))
conn.commit()

# DROP TABLE
cursor.execute("DROP TABLE IF EXISTS People")
conn.commit()

# Close the connection
cursor.close()
conn.close()