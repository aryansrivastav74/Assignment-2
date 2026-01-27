import logging

def transform_users(users):
    full_data = []
    clean_base = []

    for user in users:
        address = user.get("address", {})
        geo = address.get("geo", {})
        company = user.get("company", {})

        # -------- FULL DATA (NO VALIDATION) --------
        full_data.append({
            "id": user.get("id"),
            "name": user.get("name"),
            "username": user.get("username"),
            "email": user.get("email"),
            "phone": user.get("phone"),
            "website": user.get("website"),
            "street": address.get("street"),
            "suite": address.get("suite"),
            "city": address.get("city"),
            "zipcode": address.get("zipcode"),
            "latitude": geo.get("lat"),
            "longitude": geo.get("lng"),
            "company_name": company.get("name"),
            "company_catch_phrase": company.get("catchPhrase"),
            "company_bs": company.get("bs"),
        })

        # -------- CLEAN BASE (FOR VALIDATION) --------
        full_address = f"{address.get('street')}, {address.get('suite')}, {address.get('city')}, {address.get('zipcode')}"

        clean_base.append({
            "user_id": user.get("id"),
            "name": user.get("name"),
            "email": user.get("email"),
            "city": address.get("city"),
            "zipcode": address.get("zipcode"),
            "address": full_address,
            "phone": user.get("phone"),
            "company_name": company.get("name"),
        })

    logging.info("Transformation completed: full & clean datasets created")
    return full_data, clean_base
