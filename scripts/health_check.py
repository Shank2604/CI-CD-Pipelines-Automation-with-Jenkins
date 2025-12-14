import requests
import sys

URL = "http://localhost:8081/health"

try:
    r = requests.get(URL, timeout=5)
    if r.status_code == 200:
        print("Health check passed")
        sys.exit(0)
    else:
        print("Health check failed")
        sys.exit(1)
except Exception as e:
    print("Error:", e)
    sys.exit(1)
