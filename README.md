🚀 User Data ETL Pipeline & SQLite Integration
      Assignment #2 – Data Engineering
📌 Project Description & Overview

   In real-world data engineering, data rarely comes in a clean, ready-to-use format. APIs often return nested JSON, missing values, duplicates, or
   inconsistent fields.

   This project simulates a real-world ETL (Extract, Transform, Load) pipeline that extracts user data from an external API, cleans and validates it
   using strict business rules, stores the clean data into an SQLite relational database, and finally generates SQL-based business insights.

   By the end of execution, raw unstructured web data is converted into a structured, analysis-ready business asset.

🎯 Aim of the Project

   The main objectives of this project are to:

   Extract data from an external API using Python

   Handle unreliable data sources with proper exception handling

   Transform nested JSON data into a flat, tabular structure

   Apply strict validation rules to ensure data quality

   Implement logging to track pipeline execution and failures

   Store validated data into an SQLite relational database

   Generate meaningful business insights using SQL queries

🌐 API Used

   Source API

   https://jsonplaceholder.typicode.com/users


   This API provides nested JSON user profiles, making it ideal for ETL simulation.

🔁 Overall ETL Workflow
   API
    ↓
   Extract data (Python)
    ↓
   Transform & clean
    ↓
   Validate data
    ↓
   Save CSVs
    ↓
   Insert into SQLite (Python)
    ↓
   Run SQL insights (Python)

🧠 Step-by-Step Pipeline Flow

1️⃣ Extract (Extractor)

   Connects to the external API

   Fetches raw JSON data

   Handles API/network failures gracefully

2️⃣ Transform

   Flattens nested JSON fields (address, company)

   Combines address fields into readable format
 
   Prepares clean rows for validation

3️⃣ Validate (Quality Gates)

   Each record is validated before storage.
   Invalid records are rejected immediately to protect database integrity.

4️⃣ Load

   Saves valid records into:

   CSV files (backup)

   SQLite database (users.db)

   Uses atomic transactions to prevent partial inserts

5️⃣ Insights

   Executes SQL aggregation queries

   Produces business insights like:

   Total active users

   Most common city

   Top email domain

🛡️ Data Validation Rules
   Rule	Description	Action
   Duplicate user_id	Prevents duplicate users	❌ Reject
   Email without @	Ensures valid email format	❌ Reject
   City is null	Mandatory location field	❌ Reject
   Zipcode length < 5	Ensures valid postal code	❌ Reject

📌 Rejected records are logged in logs/pipeline.log.

🗄️ Database Design (SQLite)

   The validated data is stored in an SQLite relational database, enabling efficient querying and analysis.
   <img width="1590" height="459" alt="database" src="https://github.com/user-attachments/assets/a5fb58e3-e4c4-4ede-adff-ba0e7ba8e339" />


📂 Database File
   database/users.db

📋 Table: users
   Column	Description 
   user_id	Primary key
   name	User full name
   email	Validated email
   city	User city
   zipcode	Stored as text
   address	Combined street, suite, city
   phone	Contact number
   company_name	Company name
📸 Actual Database Output (After ETL Run)

   Screenshot below shows the final SQLite database table containing only
   validated user records after successful ETL execution.

✔ Only validated records are inserted
✔ Invalid records never pollute the database

⚙️ How the Database Works

   Database is created automatically if not present

   Uses CREATE TABLE IF NOT EXISTS

   Inserts use atomic transactions

   Maintains consistency even if failures occur

   This design mirrors production-grade ETL systems.

📁 Project File Structure

<img width="1024" height="559" alt="image" src="https://github.com/user-attachments/assets/0c29c554-2ee7-47ef-9a24-fda711994721" />

🖥️  Terminal Dashboard
<img width="2816" height="1536" alt="Gemini_Generated_Image_fom695fom695fom6" src="<img width="2816" height="1504" alt="Gemini_Generated_Image_15wl5415wl5415wl" src="https://github.com/user-attachments/assets/2f2693a5-4a88-4b69-888a-4d67d553d10b" />


  Running the pipeline gives real-time feedback for each ETL stage.

python code/main.py

  Sample Output
🚀 Starting ETL Pipeline...
📡 EXTRACT: Fetching data from API...
🔄 TRANSFORM: Processing 10 raw records...
🛡️ VALIDATE: Applying quality rules...
❌ User 3: Rejected (Zipcode too short)
✅ 9 Valid records ready for loading.
💾 LOAD: Writing to database/users.db...
✅ Data successfully saved.

--- 📊 GENERATED INSIGHTS ---
> Total Active Users: 9
> Most Common City:   Gwenborough
> Top Email Domain:   @april.biz

▶️ How to Run the Project
1️⃣ Install Dependencies
   pip install -r requirements.txt

2️⃣ Run the ETL Pipeline
   python code/main.py

3️⃣ Results

   SQLite DB → database/users.db

   Logs → logs/pipeline.log

   CSV backups → data/

✅ Assignment #2 Requirements Coverage

✔ Extract data from an external API
✔ Handle unreliable data sources
✔ Clean & transform nested JSON
✔ Apply strict data validation rules
✔ Implement logging
✔ Store data into SQLite database
✔ Generate SQL-based business insights

🏁 Conclusion

   This project demonstrates a complete ETL lifecycle using Python and SQLite, closely reflecting real-world data engineering pipelines.
   It emphasizes data quality, reliability, and analytical readiness, making it suitable for both academic evaluation and professional portfolios.
