INSERT INTO alerts
SELECT t1.transaction_id, t1.user_id, t1.amount, 'MANY_TRANSACTIONS'
FROM transactions t1
JOIN (
    SELECT user_id, COUNT(*) AS txn_count
    FROM transactions
    WHERE timestamp > CURRENT_TIMESTAMP - INTERVAL '1' MINUTE
    GROUP BY user_id
    HAVING txn_count >= 3
) t2
ON t1.user_id = t2.user_id;
