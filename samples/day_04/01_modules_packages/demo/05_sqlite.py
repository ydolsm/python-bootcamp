import sqlite3

# Connect to a database (or create it if it doesn't exist)
connection = sqlite3.connect("demo.db")
cursor = connection.cursor()

# Create a table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
)
""")
connection.commit()

# Insert data
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 25))
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Bob", 30))
connection.commit()

# Query data
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
print("Users in the database:")
for row in rows:
    print(row)

# Close the connection
connection.close()
