import requests
import sys

URL = "http://host.docker.internal:8000/health"

try:
    r = requests.get(URL)

    if r.status_code == 200:
        print("PASS")
        sys.exit(0)

    else:
        print("FAIL")
        sys.exit(1)

except Exception as e:
    print("ERROR", e)
    sys.exit(1)