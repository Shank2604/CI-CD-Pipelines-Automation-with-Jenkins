import time

LOG_FILE = "/var/log/app.log"

with open(LOG_FILE, "r") as f:
    lines = f.readlines()[-10:]

for line in lines:
    if "ERROR" in line:
        print("Error found in logs")
