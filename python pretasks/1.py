import mysql.connector

# Establishing a connection to the MySQL database
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mysql"  # We'll initially connect to the 'mysql' database to execute administrative commands
)

# Creating a cursor object to execute SQL queries
cursor = connection.cursor()

# Creating the user with limited rights
try:
    cursor.execute("CREATE USER 'limited_user'@'localhost' IDENTIFIED BY 'password'")
    cursor.execute("GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, ALTER, INDEX, DROP, EVENT, TRIGGER ON your_database.* TO 'limited_user'@'localhost'")
    print("User 'limited_user' created with limited rights.")
except mysql.connector.Error as err:
    print("Error:", err)

# Closing the cursor and connection
cursor.close()
connection.close()
