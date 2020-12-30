import gspread
from ProfileFinder import getProfile
from oauth2client.service_account import ServiceAccountCredentials

# Credentials to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.

sheet = client.open("LinkedIn RED TC").get_worksheet(0)

def addRow(candidateLink, userName, userAccount, userPassword):
    try:
        candidateName, candidateCharge, candidateID = getProfile(candidateLink, userAccount, userPassword)
    except:
        return
    row = [candidateName, candidateCharge, candidateID, userName, userAccount]
    nextRow = len(sheet.get_all_values()) + 1
    sheet.insert_row(row, nextRow)
