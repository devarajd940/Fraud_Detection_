CREATE TABLE alerts (
    transaction_id STRING,
    user_id STRING,
    amount DOUBLE,
    alert_reason STRING
) WITH (
    'connector' = 'kafka',
    'topic' = 'alerts',
    'properties.bootstrap.servers' = 'localhost:9092',
    'format' = 'json'
);
