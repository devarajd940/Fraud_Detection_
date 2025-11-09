from kafka import KafkaConsumer
import json
import threading

def consume_topic(topic):
    consumer = KafkaConsumer(
        topic,
        bootstrap_servers='localhost:9092',
        auto_offset_reset='earliest',
        value_deserializer=lambda m: json.loads(m.decode('utf-8'))
    )
    print(f"Consuming from topic: {topic}")
    for message in consumer:
        print(f"{topic} message:", message.value)

# Run consumers in separate threads
threading.Thread(target=consume_topic, args=('transactions',), daemon=True).start()
threading.Thread(target=consume_topic, args=('alerts',), daemon=True).start()

# Keep the main thread alive
import time
while True:
    time.sleep(1)
