from numpy.random import normal
from random import choice
from datetime import datetime, timezone  

class Transaction:

    def __init__(self, sender, receiver, amount, time):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.time = time

    def serialize(self):
        return "transaction,sender={sender},receiver={receiver} amount={amount:.2f} {time}" \
            .format(sender=self.sender,
                    receiver=self.receiver,
                    amount=self.amount,
                    time=self.time)
    
    def encode(self, encoding="utf-8"):
        return self.serialize().encode(encoding)

    def __repr__(self):
        return self.serialize()

    def __str__(self):
        return self.serialize()

class TransactionFactory:
    """
    This class samples a series of bank transactions.
    """

    def __init__(self):
        self.customers = ["Alice", "Bob", "Carl", "James", "Claire", "Jasmine"]

    def sampleTransaction(self):
        return Transaction(
            choice(self.customers),
            choice(self.customers),
            self.__amount(),
            self.__time()
        )

    def __amount(self):
        return normal(50, 10, 1)[0]

    def __time(self):
        # unix time ms
        return int(datetime.now(tz=timezone.utc).timestamp() * 1000)