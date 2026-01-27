import csv
import logging
import os
import sqlite3

# -------- SAVE FULL CSV --------
def save_full_csv(users, file_path):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    fieldnames = [
        "id","name","username","email","phone","website",
        "street","suite","city","zipcode",
        "latitude","longitude",
        "company_name","company_catch_phrase","company_bs"
    ]

    with open(file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(users)

    logging.info("Full CSV saved successfully")


# -------- SAVE CLEAN CSV --------
def save_to_csv(users, file_path):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    fieldnames = [
        "user_id","name","email","city","zipcode",
        "address","phone","company_name"
    ]

    with open(file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(users)

    logging.info("Clean CSV saved successfully")


# -------- INSERT INTO SQLITE --------
def insert_into_db(users, db_path):
    os.makedirs(os.path.dirname(db_path), exist_ok=True)

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS users")

    cursor.execute("""
        CREATE TABLE users (
            user_id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT,
            city TEXT,
            zipcode TEXT,
            address TEXT,
            phone TEXT,
            company_name TEXT
        )
    """)

    for user in users:
        cursor.execute("""
            INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            user["user_id"],
            user["name"],
            user["email"],
            user["city"],
            user["zipcode"],
            user["address"],
            user["phone"],
            user["company_name"]
        ))

    conn.commit()
    conn.close()
    logging.info("Clean data inserted into SQLite")
