from kafka.admin import KafkaAdminClient, NewTopic

admin_client = KafkaAdminClient(
    bootstrap_servers='localhost:9092',
    client_id='admin_client'
)

topic = NewTopic(
    name='alerts_filter',
    num_partitions=1,
    replication_factor=1
)

try:
    admin_client.create_topics([topic])
    print("Topic 'alerts_filter' created")
except Exception as e:
    print("Topic creation error:", e)
