from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import requests

class Crypto:
    def __init__(self, public_key_url):
        pk = requests.get(public_key_url)
        print("Public Key")
        print(pk.text)
        public_key = serialization.load_pem_public_key(
            pk.content,
            backend=default_backend()
        )
        self.public_key = public_key

    def encrypt(self, message):
        encrypted = self.public_key.encrypt(
            message,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return encrypted
        