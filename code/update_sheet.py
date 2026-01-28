import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

CSV_PATH = "data/users_clean.csv"
SHEET_NAME = "Users Clean Data"  
CREDENTIALS_FILE = "credentials.json"


scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

creds = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE, scope
)
client = gspread.authorize(creds)


df = pd.read_csv(CSV_PATH)


sheet = client.open(SHEET_NAME)
worksheet = sheet.sheet1


worksheet.clear()


worksheet.update(
    [df.columns.values.tolist()] + df.values.tolist()
)

print("✅ Google Sheet updated successfully from CSV!")
print("📄 Sheet URL:", sheet.url)
