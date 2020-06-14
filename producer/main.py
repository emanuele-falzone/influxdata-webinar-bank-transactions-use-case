import os
from time import sleep
from random import uniform
from kafka import KafkaProducer

from transaction import TransactionFactory
from crypto import Crypto

if __name__ == "__main__":
    broker = os.environ['KAFKA_BROKER']
    topic = os.environ['KAFKA_TOPIC']
    public_key_url = os.environ['PUBLIC_KEY_URL']
    print("Using {} as Kafka Broker".format(broker))
    print("Using {} as Kafka Topic".format(topic))
    print("Using {} as public key".format(public_key_url))

    c = Crypto(public_key_url)
    print("Public key loaded!")

    producer = KafkaProducer(
        bootstrap_servers=broker,
        value_serializer=c.encrypt
    )
    print("Kafka Producer is ready!")

    factory = TransactionFactory()

    while True:
        transaction = factory.sampleTransaction()
        print(transaction)
        producer.send(topic, transaction.encode())
        sleep(uniform(0.5, 2))
