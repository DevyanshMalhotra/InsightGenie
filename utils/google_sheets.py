import pandas as pd
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

def connect_google_sheet(sheet_url):
    # Path to your service account JSON file
    SERVICE_ACCOUNT_FILE = "service_account.json"

    # Define the required scopes
    SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

    # Authenticate with the service account
    credentials = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    # Extract the Google Sheet ID from the URL
    sheet_id = sheet_url.split("/")[5]

    # Connect to the Google Sheets API
    service = build("sheets", "v4", credentials=credentials)
    sheet = service.spreadsheets()
    
    # Read data from the first sheet
    result = sheet.values().get(spreadsheetId=sheet_id, range="Sheet1").execute()
    values = result.get("values", [])

    # Convert data to a Pandas DataFrame
    if values:
        df = pd.DataFrame(values[1:], columns=values[0])  # First row as column headers
        return df
    return pd.DataFrame()
