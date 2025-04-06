import requests
import time

url = "https://www.google.com"
while True:
    try:
        response = requests.get(url)
        print(f"{time.ctime()}: {url} is UP - Status {response.status_code}")
    except requests.exceptions.RequestException:
        print(f"{time.ctime()}: {url} is DOWN")
    time.sleep(60)
