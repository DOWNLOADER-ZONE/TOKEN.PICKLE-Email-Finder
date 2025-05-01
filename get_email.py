import pickle
from googleapiclient.discovery import build

with open('token.pickle', 'rb') as token_file:
    creds = pickle.load(token_file)

try:
    service = build('drive', 'v3', credentials=creds)
    about = service.about().get(fields="user").execute()
    print("Email address:", about['user']['emailAddress'])
except Exception as e:
    print("Failed to fetch email from Drive API:", e)
