from Iterables import Iterables
from collections import OrderedDict

class Transactions(Iterables):
    """
    This class manages the Tranasaction in each Block of the Blockchain.
    Attributes:
        sender: Sender of the Transaction.
        recipient: Recipient of the Transaction.
        amount: Amount of the Transaction.
    """
    def __init__(self, sender, recipient, amount):
        """
		This function initialise the Transaction.
		Attributes:
        sender: Sender of the Transaction.
        recipient: Recipient of the Transaction.
        amount: Amount of the Transaction.
		"""
        self.sender = sender
        self.recipient = recipient
        self.amount = amount

    def make_ordered(self):
        """
        This functions converts the transaction object to Ordered Dictionary objects.
        Returns:
            The OrderedDict() object of the transaction.
        """
        return OrderedDict([("sender",self.sender),("recipient",self.recipient),("amount",self.amount)])