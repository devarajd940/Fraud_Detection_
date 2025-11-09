import requests

data = {
    "TransactionID": "1001",
    "AccountID": "A1",
    "TransactionAmount": 5000,
    "TransactionDate": "2025-10-29T00:12:00",
    "TransactionType": "debit",
    "Location": "Mumbai",
    "DeviceID": "D123",
    "IP Address": "1.2.3.4",
    "MerchantID": "M001",
    "Channel": "ATM",
    "CustomerAge": 34,
    "CustomerOccupation": "Engineer",
    "TransactionDuration": 20,
    "LoginAttempts": 1,
    "AccountBalance": 60000,
    "PreviousTransactionDate": "2025-10-28T12:00:00"
}
resp = requests.post("http://localhost:7861/api/v1/webhook/c9541387-dc92-4a2e-ab54-0fabb265f185", json=data)
print(resp.status_code, resp.text)
