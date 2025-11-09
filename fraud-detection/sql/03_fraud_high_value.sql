INSERT INTO alerts
SELECT transaction_id, user_id, amount, 'HIGH_AMOUNT'
FROM transactions
WHERE amount > 10000;
