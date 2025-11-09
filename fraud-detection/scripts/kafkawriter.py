from kafka import KafkaConsumer, KafkaProducer
import json

consumer = KafkaConsumer(
    'alerts',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda m: json.dumps(m).encode('utf-8')
)

print("Starting to consume alerts and filter TransactionAmount > 1000...")

for msg in consumer:
    event = msg.value
    if event.get('TransactionAmount', 0) > 1000:
        producer.send('alerts_filter', value=event)
        print("Forwarded filtered event:", event)
