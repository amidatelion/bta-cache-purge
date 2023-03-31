import requests
import time

S = requests.Session()

FILE_URL = "https://bta3062.com/files/list_of_mechs.txt"
API_URL = "https://bta3062.com/api.php"

# Fetching the text file from the URL
response = requests.get(FILE_URL)

if response.status_code != 200:
    print("Failed to fetch the text file")
    exit()

# Splitting the text file into lines and iterating over each line
for line in response.text.split('\n'):
    # Skipping empty lines
    if not line:
        continue

    PARAMS = {
        "action": "purge",
        "titles": line,
        "format": "json"
    }

    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    R = S.post(url=API_URL, params=PARAMS, headers=headers)
    DATA = R.text

    print(DATA)

    # Sleeping for 10 seconds
    time.sleep(10)
