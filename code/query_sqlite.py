import sqlite3

conn = sqlite3.connect("database/users.db")
cursor = conn.cursor()

print("✅ Connected to SQLite database")


print("\n📄 All users:")
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)

print("\n📄 User names and emails:")
cursor.execute("""
    SELECT name, email
    FROM users
""")
for row in cursor.fetchall():
    print(row)


print("\n📄 Business users (.biz emails):")
cursor.execute("""
    SELECT name, email
    FROM users
    WHERE email LIKE '%.biz'
""")
for row in cursor.fetchall():
    print(row)

print("\n📊 Users per city:")
cursor.execute("""
    SELECT city, COUNT(*)
    FROM users
    GROUP BY city
""")
for row in cursor.fetchall():
    print(row)


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

conn.close()
print("\n✅ Database connection closed")

