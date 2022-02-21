from hash_util import get_hash,hash_str

h=[] 
class Verifier:
    """
		This class contains various functions to verify the integrity of the Blockchain.
    """

    def verify_transaction(self,transaction,get_balance):
        """
		This function verifies the integrity of a transaction.
        Attributes:
            transaction: The transaction that is about to be added.
            get_balance: Function to calculate balance of a particular user.
        Returns:
            Returns True if the transaction is valid else False.
        """
        if transaction.amount > get_balance(transaction.sender):
            return False
        return True

    def is_valid(self, blockchain):
        """
		This function validates the integrity of the Blockchain.
        Attributes:
            blockchain: The Blockchain.
        Returns:
            Returns True if the blockchain is valid else False.
        """
        for index,block in enumerate(blockchain):
            if index == 0:
                continue
            if block.previous_hash != get_hash(blockchain[index - 1]):
                return False
            if not self.valid_proof(block.transactions[:-1], block.previous_hash, block.proof):
                print('Invalid Proof')
                return False
        return True

    def valid_proof(self, transactions, pre_hash, proof):
        """
		This function validates the proof number required to mine a Block.
        Attributes:
            transactions: List of Transactions.
            pre_hash: Hash of previous Block in the Blockchain.
            proof: Proof number to be validated.
        Returns:
            Returns True if the proof number satisfies the Algorithm.
        """
        global h
        s = str([t.make_ordered() for t in transactions]) + str(pre_hash) +str(proof)
        test_hash = hash_str(s.encode())
        if test_hash[0:3] == "00b":
            h.append(test_hash)
            return True
        else:
            return False
        
    @staticmethod
    def get_test_hash():
        global h
        return h