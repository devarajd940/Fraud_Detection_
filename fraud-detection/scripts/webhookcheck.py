import requests

data = {"test": "webhook", "value": 42}
response = requests.post(
    "http://localhost:7861/api/v1/webhook/c9541387-dc92-4a2e-ab54-0fabb265f185",
    json=data
)
print(response.status_code, response.text)
