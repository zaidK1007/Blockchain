from time import time
from Iterables import Iterables

class Block(Iterables):
    """
    This class manages the blocks in the blockchain.
    
    Attributes:
        previous_hash: Hash of the previous block.
        index: Index of the block.
        transactions: Transactions in a block.
        proof: Proof number of the block.
        timestamp: Timestamp of the block.
    """
    def __init__(self, previous_hash, index, transactions, proof, timestamp=time()):
        """
        This  function initialise a Block in blockchain.

        Attributes:
            previous_hash: Hash of the previous block.
            index: Index of the block.
            transactions: Transactions in a block.
            proof: Proof number of the block.
            timestamp: Timestamp of the block.
        """
        self.previous_hash = previous_hash
        self.index = index
        self.transactions = transactions
        self.proof = proof
        self.timestamp = timestamp