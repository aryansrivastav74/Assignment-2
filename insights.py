import sqlite3

def users_per_city(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT city, COUNT(*) FROM users GROUP BY city
    """)
    result = cursor.fetchall()
    conn.close()
    return result


def business_email_users(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT name, email FROM users WHERE email LIKE '%.biz'
    """)
    result = cursor.fetchall()
    conn.close()
    return result
