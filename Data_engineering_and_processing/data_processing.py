# Data Processing using Kafka

from kafka import KafkaProducer, KafkaConsumer
import json
import time
import random

# Kafka Producer
def produce_data():
    producer = KafkaProducer(
        bootstrap_servers='localhost:9092',
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

    while True:
        data = {
            'device_id': f'device_{random.randint(1, 10)}',
            'timestamp': time.time(),
            'value': random.uniform(20.0, 30.0)
        }
        producer.send('iot_data', data)
        print(f"Produced: {data}")
        time.sleep(1)

# Kafka Consumer
def consume_data():
    consumer = KafkaConsumer(
        'iot_data',
        bootstrap_servers='localhost:9092',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )

    for message in consumer:
        data = message.value
        print(f"Consumed: {data}")

if __name__ == "__main__":
    # Uncomment one of the following lines to run the producer or consumer
    # produce_data()
    consume_data()
