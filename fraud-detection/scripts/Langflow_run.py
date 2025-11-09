from kafka import KafkaConsumer
import requests
import json
import time

consumer = KafkaConsumer(
    'fraud_alerts',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=False,
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

for msg in consumer:
    requests.post(
        "http://localhost:7861/api/v1/webhook/b98145f1-18ce-40e5-b4d7-c9f97a126996",
        json=msg.value
    )
    print("Sent alert:", msg.value)
    time.sleep(5.0)  # 5 second delay after each message