from kafka import KafkaProducer
import json
producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))
message = {'test_key': 'hello_kafka'}
print("Attempting to send one message...")
try:
    future = producer.send('test-topic', message)
    record_metadata = future.get(timeout=10) # Wait for confirmation
    print(f"Message sent successfully! Offset: {record_metadata.offset}")
except Exception as e:
    print(f"Failed to send message: {e}")
producer.close()
print("Producer finished.")
