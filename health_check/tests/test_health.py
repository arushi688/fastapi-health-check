import requests
import sys

response = requests.get("http://localhost:8000/health")

print("Status Code:", response.status_code)

if response.status_code != 200:
    sys.exit(1)

print("Health check passed")