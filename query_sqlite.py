import sqlite3

# Step 1: Connect to SQLite database
conn = sqlite3.connect("database/users.db")
cursor = conn.cursor()

print("✅ Connected to SQLite database")

# Step 2: Retrieve all users
print("\n📄 All users:")
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Step 3: Retrieve selected columns
print("\n📄 User names and emails:")
cursor.execute("""
    SELECT name, email
    FROM users
""")
for row in cursor.fetchall():
    print(row)

# Step 4: Business users (.biz emails)
print("\n📄 Business users (.biz emails):")
cursor.execute("""
    SELECT name, email
    FROM users
    WHERE email LIKE '%.biz'
""")
for row in cursor.fetchall():
    print(row)

# Step 5: Users per city (aggregation)
print("\n📊 Users per city:")
cursor.execute("""
    SELECT city, COUNT(*)
    FROM users
    GROUP BY city
""")
for row in cursor.fetchall():
    print(row)

# Step 6: Data quality check
print("\n🔍 Invalid records check:")
cursor.execute("""
    SELECT *
    FROM users
    WHERE city IS NULL
       OR email NOT LIKE '%@%'
       OR LENGTH(zipcode) < 5
""")
invalid = cursor.fetchall()
print(invalid)

# Step 7: Close connection
conn.close()
print("\n✅ Database connection closed")

