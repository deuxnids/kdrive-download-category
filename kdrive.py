import os
from dotenv import load_dotenv
import requests

load_dotenv()

KDRIVE_TOKEN = os.getenv('token')
DRIVE_ID = os.getenv("DRIVE_ID")

CATEGORY_ID=38
destination_directory_id=131269

headers = {
  'Authorization': f'Bearer {KDRIVE_TOKEN}',
  'Content-Type': 'application/json',
}

CURSOR = None

URL = f"https://api.infomaniak.com/3/drive/{DRIVE_ID}/files/search?limit=100&category={CATEGORY_ID}"

has_more = True

files = []

while has_more:

    url = URL
    if CURSOR is not None:
        url = url + f"&cursor={CURSOR}"
    req = requests.request("GET", url = url , headers = headers)
    res = req.json()
    files +=  res["data"] 
    has_more =res["has_more"]
    CURSOR =res["cursor"]

for file in files:
    URL = f"https://api.infomaniak.com/3/drive/{DRIVE_ID}/files/{file['id']}/copy/{destination_directory_id}"
    data = {"name": file["name"]}
    req = requests.request("POST", url = URL , json = data, headers = headers)
    res = req.json()
    print(res)