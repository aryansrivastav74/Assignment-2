import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# ========== CONFIG ==========
CSV_PATH = "data/users_clean.csv"
SHEET_NAME = "Users Clean Data"   # Existing Google Sheet name
CREDENTIALS_FILE = "credentials.json"

# ========== AUTH ==========
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

creds = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE, scope
)
client = gspread.authorize(creds)

# ========== LOAD CSV ==========
df = pd.read_csv(CSV_PATH)

# ========== OPEN SHEET ==========
sheet = client.open(SHEET_NAME)
worksheet = sheet.sheet1

# ========== CLEAR OLD DATA ==========
worksheet.clear()

# ========== UPDATE WITH CSV DATA ==========
worksheet.update(
    [df.columns.values.tolist()] + df.values.tolist()
)

print("✅ Google Sheet updated successfully from CSV!")
print("📄 Sheet URL:", sheet.url)
