CREATE TABLE transactions (
    transaction_id STRING,
    user_id STRING,
    amount DOUBLE,
    `timestamp` TIMESTAMP(3),
    location STRING,
    WATERMARK FOR `timestamp` AS `timestamp` - INTERVAL '5' SECOND
) WITH (
    'connector' = 'kafka',
    'topic' = 'transactions-data',
    'properties.bootstrap.servers' = 'localhost:9092',
    'value.format' = 'json',
    'scan.startup.mode' = 'earliest-offset'
);

CREATE TABLE alerts (
    transaction_id STRING,
    user_id STRING,
    amount DOUBLE,
    alert_reason STRING,
    alert_time TIMESTAMP_LTZ(3) METADATA FROM 'timestamp' VIRTUAL
) WITH (
    'connector' = 'kafka',
    'topic' = 'alerts',
    'properties.bootstrap.servers' = 'localhost:9092',
    'value.format' = 'json'
);

INSERT INTO alerts
SELECT transaction_id, user_id, amount, 'HIGH_AMOUNT'
FROM transactions
WHERE amount > 10000;

INSERT INTO alerts
SELECT
    t.transaction_id,
    t.user_id,
    t.amount,
    'MANY_TRANSACTIONS_1MIN'
FROM transactions t
JOIN (
    SELECT
        user_id,
        window_start,
        window_end,
        COUNT(*) AS txn_count
    FROM TABLE(
        HOP(TABLE transactions, DESCRIPTOR(`timestamp`), INTERVAL '20' SECOND, INTERVAL '1' MINUTE)
    )
    GROUP BY user_id, window_start, window_end
    HAVING COUNT(*) >= 3
) w
ON t.user_id = w.user_id
AND t.`timestamp` >= w.window_start
AND t.`timestamp` <  w.window_end;
