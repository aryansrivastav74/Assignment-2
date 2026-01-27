import logging

def validate_users(users):
    valid_users = []
    seen_ids = set()

    for user in users:

        # Rule 1: Duplicate user_id
        if user["user_id"] in seen_ids:
            logging.warning(f"Duplicate user_id rejected: {user['user_id']}")
            continue

        # Rule 2: Email without '@'
        if "@" not in user["email"]:
            logging.warning(f"Invalid email rejected: {user['email']}")
            continue

        # Rule 3: City null
        if not user["city"]:
            logging.warning(f"City null rejected for user_id: {user['user_id']}")
            continue

        # Rule 4: Zipcode length < 5
        if not user["zipcode"] or len(user["zipcode"]) < 5:
            logging.warning(f"Invalid zipcode rejected for user_id: {user['user_id']}")
            continue

        seen_ids.add(user["user_id"])
        valid_users.append(user)

    logging.info(f"Validation completed. Valid records: {len(valid_users)}")
    return valid_users
