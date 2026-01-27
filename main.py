import logging
import os

from extractor import extract_users
from transformer import transform_users
from validator import validate_users
from loader import save_full_csv, save_to_csv, insert_into_db
from insights import users_per_city, business_email_users

# -------- LOGGING --------
os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

API_URL = "https://jsonplaceholder.typicode.com/users"
FULL_CSV_PATH = "data/users_full.csv"
CLEAN_CSV_PATH = "data/user_clean.csv"
DB_PATH = "database/users.db"


def main():
    raw_data = extract_users(API_URL)

    full_data, clean_base = transform_users(raw_data)

    # Save FULL CSV (no validation)
    save_full_csv(full_data, FULL_CSV_PATH)

    # Validate & save CLEAN CSV
    validated_data = validate_users(clean_base)
    save_to_csv(validated_data, CLEAN_CSV_PATH)

    # Insert clean data into SQLite
    insert_into_db(validated_data, DB_PATH)

    # -------- SQL INSIGHTS --------
    print("Users per city:")
    for row in users_per_city(DB_PATH):
        print(row)

    print("\nUsers with business emails:")
    for row in business_email_users(DB_PATH):
        print(row)

    logging.info("Pipeline executed successfully")


if __name__ == "__main__":
    main()
