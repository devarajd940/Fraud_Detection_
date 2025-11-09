import csv
import time
import json
from datetime import datetime
from kafka import KafkaProducer


def on_send_success(record_metadata):
    print(f"Success! Topic: {record_metadata.topic}, Partition: {record_metadata.partition}, Offset: {record_metadata.offset}")

def on_send_error(excp):
    print(f"ERROR: Message failed to send: {excp}")


producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

csv_file_path = 'bank_transactions_data_2.csv'
transactions_topic = 'bank_transactions'

print(f"Starting to stream data from {csv_file_path}...")

try:
    with open(csv_file_path, mode='r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                # Parse/normalize TransactionDate and PreviousTransactionDate
                # TransactionDate
                transaction_date_str = row.get('TransactionDate')
                try:
                    transaction_date = datetime.strptime(transaction_date_str, '%Y-%m-%d %H:%M:%S')
                except ValueError:
                    transaction_date = datetime.strptime(transaction_date_str, '%d/%m/%y %H:%M')
                transaction_date_formatted = transaction_date.strftime('%Y-%m-%d %H:%M:%S')

                # PreviousTransactionDate
                prev_transaction_date_str = row.get('PreviousTransactionDate')
                if prev_transaction_date_str:
                    try:
                        prev_transaction_date = datetime.strptime(prev_transaction_date_str, '%Y-%m-%d %H:%M:%S')
                    except ValueError:
                        prev_transaction_date = datetime.strptime(prev_transaction_date_str, '%d/%m/%y %H:%M')
                    prev_transaction_date_formatted = prev_transaction_date.strftime('%Y-%m-%d %H:%M:%S')
                else:
                    prev_transaction_date_formatted = None

                # Build the message dictionary with all requested fields
                message = {
                    'TransactionID': row.get('TransactionID'),
                    'AccountID': row.get('AccountID'),
                    'TransactionAmount': float(row.get('TransactionAmount', 0.0)),
                    'TransactionDate': transaction_date_formatted,
                    'TransactionType': row.get('TransactionType'),
                    'Location': row.get('Location'),
                    'DeviceID': row.get('DeviceID'),
                    'IP Address': row.get('IP Address'),
                    'MerchantID': row.get('MerchantID'),
                    'Channel': row.get('Channel'),
                    'CustomerAge': row.get('CustomerAge'),
                    'CustomerOccupation': row.get('CustomerOccupation'),
                    'TransactionDuration': row.get('TransactionDuration'),
                    'LoginAttempts': row.get('LoginAttempts'),
                    'AccountBalance': row.get('AccountBalance'),
                    'PreviousTransactionDate': prev_transaction_date_formatted
                }

                producer.send(transactions_topic, message).add_callback(on_send_success).add_errback(on_send_error)
                time.sleep(0.01)

            except (ValueError, TypeError) as e:
                print(f"Skipping a malformed row: {row}. Error: {e}")
                continue

except FileNotFoundError:
    print(f"ERROR: The file '{csv_file_path}' was not found. Make sure it's in the same directory as the script.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("Flushing all messages...")
    producer.flush()
    producer.close()
    print("Producer closed.")
