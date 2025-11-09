from kafka import KafkaProducer
import json

producer = KafkaProducer(bootstrap_servers='localhost:9092')

messages = [
    {"transaction_id":"TX002195","user_id":"AC00418","amount":1047.69,"timestamp":"2023-10-16 16:32:31","location":"Austin"},
{"transaction_id":"TX002202","user_id":"AC00385","amount":1431.54,"timestamp":"2023-12-11 16:23:59","location":"Portland"},
{"transaction_id":"TX002216","user_id":"AC00290","amount":1413.24,"timestamp":"2023-11-06 18:59:24","location":"New York"},
{"transaction_id":"TX002228","user_id":"AC00291","amount":1152.58,"timestamp":"2023-09-13 17:58:16","location":"Austin"},
{"transaction_id":"TX002243","user_id":"AC00252","amount":1169.59,"timestamp":"2023-12-25 17:12:21","location":"New York"},
{"transaction_id":"TX002268","user_id":"AC00416","amount":1360.67,"timestamp":"2023-04-19 16:38:41","location":"Raleigh"},
{"transaction_id":"TX002273","user_id":"AC00268","amount":1454.52,"timestamp":"2023-09-22 16:13:06","location":"Miami"},
{"transaction_id":"TX002277","user_id":"AC00093","amount":1021.38,"timestamp":"2023-01-27 18:59:43","location":"Detroit"},
{"transaction_id":"TX002293","user_id":"AC00388","amount":1030.85,"timestamp":"2023-09-04 17:22:24","location":"San Diego,"},
{"transaction_id":"TX002305","user_id":"AC00494","amount":1142.76,"timestamp":"2023-03-15 17:10:12","location":"Houston"},
{"transaction_id":"TX002335","user_id":"AC00016","amount":1105.88,"timestamp":"2023-03-06 17:37:32","location":"Omaha"},
{"transaction_id":"TX002343","user_id":"AC00420","amount":1021.16,"timestamp":"2023-10-16 17:32:16","location":"Albuquerque"},
{"transaction_id":"TX002381","user_id":"AC00098","amount":1173.74,"timestamp":"2023-09-25 16:44:52","location":"Virginia Beach"},
{"transaction_id":"TX002404","user_id":"AC00111","amount":1493.0,"timestamp":"2023-06-07 17:05:41","location":"Colorado Springs"},
{"transaction_id":"TX002415","user_id":"AC00028","amount":1664.33,"timestamp":"2023-09-25 17:11:19","location":"San Antonio"}
]

for message in messages:
    producer.send('your-topic-name', value=json.dumps(message).encode('utf-8'))

producer.flush()
