import sqlite3

# Step 1: Open or create a database file
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

# Step 2: Make a table called 'users' if it doesn’t already exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE
    )
''')

# Step 3: Delete all old records from the 'users' table (for testing)
cursor.execute("DELETE FROM users")

# Step 4: Add two users into the table
cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("John", "john@example.com"))
cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("Sara", "sara@example.com"))

# Step 5: Save changes and show all users
conn.commit()
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()