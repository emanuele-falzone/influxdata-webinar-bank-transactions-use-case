import os
import requests
from time import sleep
from random import uniform
from kafka import KafkaConsumer
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

class Crypto:
    def __init__(self, private_key_url):
        pk = requests.get(private_key_url)
        print("Private Key")
        print(pk.text)

        private_key = serialization.load_pem_private_key(
            pk.content,
            password=None,
            backend=default_backend()
        )
        self.private_key = private_key

    def decrypt(self, encrypted):
        original_message = self.private_key.decrypt(
            encrypted,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return original_message

if __name__ == "__main__":
    broker = os.environ['KAFKA_BROKER']
    topic = os.environ['KAFKA_TOPIC']
    private_key_url = os.environ['PRIVATE_KEY_URL']
    print("Using {} as Kafka Broker".format(broker))
    print("Using {} as Kafka Topic".format(topic))
    print("Using {} as private key".format(private_key_url))

    c = Crypto(private_key_url)
    print("Private key loaded!")

    consumer = KafkaConsumer(
        bootstrap_servers=broker,
        value_deserializer=c.decrypt
    )
    consumer.subscribe([topic])

    print("Kafka Consumer is ready!")

    for message in consumer:
        print(message)