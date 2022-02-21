from Block import Block
from Transactions import Transactions
from Verification import Verifier
from testing import Testing

import functools
from hash_util import get_hash, hash_str
from collections import OrderedDict 
import json


participants = {'Zaid'}
REWARD = 10

class Blockchain:
	"""
	This Blockchain class manages the structure of the whole chain, the 
	uncommitted transactions and also the node on which its running.
	
	Attributes:
	__chain : The list of Block objects in the blockchain.
	__open_transactions: The list of Transactions that are uncommitted 
	user: Name of the user.
	"""
	def __init__(self, user):
		"""
		This function initialise the Blockchain.

		Attributes:
		user: Name of the user
		"""
		genesis_block = Block('',0, [], 1007, 1)
		self.user  = user
		self.__chain = [genesis_block]
		self.__open_transactions = []
		self.load_data()
	
	def set_chain(self,chain):
		"""
		Setter for the Blockchain.

		Attributes:
		chain: new chain to be set
		"""
		self.__chain = chain
	
	def get_chain(self):
		"""
		Returns a copy of a Blockchain.
		"""
		return self.__chain[:]


	def add_transaction(self,recipient, amount, sender):
		"""
		This function adds a transaction to the list of Uncommitted Transactions.
		
		Returns:
			True if the transaction is valid else False

		Attributes:
			recipient: Name of the recipient.
			amount: Amount to be sent.
			sender: Name of the sender.
		"""
		transaction = Transactions(sender,recipient,amount)
		v = Verifier()
		if v.verify_transaction(transaction,self.get_balance):
			self.__open_transactions.append(transaction)
			participants.add(sender)
			participants.add(recipient)
			self.save_data()
			return True
		else:
			return False

	def mine_block(self):
		"""
		This function mines a block and adds it to the Blockchain.
		"""
		last_block = self.__chain[-1]
		proof = self.proof_of_work()
		reward_trans = Transactions("SYSTEM",self.user,10)
		cpy_trans = self.__open_transactions[:]
		cpy_trans.append(reward_trans)
		block = Block(get_hash(last_block), len(self.__chain), cpy_trans, proof)
		self.__chain.append(block)
		self.__open_transactions = []
		self.save_data()

	def get_balance(self, participant):
		"""
		This function calculates the balance of a particular user.
		
		Returns:
			The balance of the User.
		Attributes:
			participant: User
		"""
		sent = [[t.amount for t in block.transactions if t.sender == participant] for block in self.__chain]
		open_sent = [t.amount for t in self.__open_transactions if t.sender == participant]
		reci = [[t.amount for t in block.transactions if t.recipient == participant] for block in self.__chain]
		sent.append(open_sent)
		amt_sent = functools.reduce(lambda s,el:s+sum(el) if len(el) > 0 else s+0,sent,0)
		amt_reci = functools.reduce(lambda s,el:s+sum(el) if len(el) > 0 else 0,reci,0)
		return amt_reci - amt_sent



	def proof_of_work(self):
		"""
		This function calculates the PROOF OF WORK required to add a block to the Blockchain.
		Returns:
			Valid proof number.
		"""
		proof = 0
		last_block = self.__chain[-1]
		while not Verifier().valid_proof(self.__open_transactions, get_hash(last_block), proof):
			proof += 1
		return proof

	def save_data(self):
		"""
		This function saves the Blockchain data to the disk in JSON format.
		"""
		try:
			with open('blockchain.txt', mode='w') as f:
				up_chain = []
				for el in self.__chain:
					blk = Block(el.previous_hash,el.index,[t.__dict__ for t in el.transactions], el.proof, el.timestamp)
					up_chain.append(blk.__dict__)
				f.write(json.dumps(up_chain))
				f.write('\n')
				up_tx = [t.__dict__ for t in self.__open_transactions]
				f.write(json.dumps(up_tx))
				self.formattedData()
		except IOError:
			print('Saving Failed')

	def formattedData(self):
		"""
		This function writes the data stored in the chain in proper readable format. 
		"""
		try:
			with open('chain_data.txt', mode='w') as f:
				
				for i,el in enumerate(self.__chain):
					f.write('-'*15)
					f.write('Block: {}'.format(i+1))
					f.write('-'*15)
					f.write('\n')
					f.write(f'Previous Hash: {el.previous_hash}')
					f.write('\n')
					f.write(f'Transactions: {el.transactions}')
					f.write('\n')
					f.write(f'Proof of Work: {el.proof}')
					f.write('\n')
					f.write(f'Timestamp: {el.timestamp}')
					f.write('\n')
					f.write(f'Hash_Satisfying_Proof: {Verifier.get_test_hash()[-1]}')
					f.write('\n')

		except IOError:
			print('Formatting Failed')
		
	def load_data(self):
		"""
		This function loads the data from the disk.
		"""
		try:
			with open('blockchain.txt', mode='r') as f:
				data = f.readlines()
				if len(data) > 0:
					blockchain = json.loads(data[0][:-1])
					up_blockchain = []
					for block in blockchain:
						up_block = Block(block['previous_hash'],block['index'],
						[Transactions(t['sender'],t['recipient'],t['amount']) for t in block['transactions']], block['proof'],block['timestamp'])
						
						up_blockchain.append(up_block)

					self.__chain = up_blockchain
					open_tx = json.loads(data[1])
					up_transactions = []
					for t in open_tx:
						up_t = Transactions(t['sender'],t['recipient'],t['amount'])
						up_transactions.append(up_t)
					self.__open_transactions = up_transactions
		except IOError:
			print('File not found')
		








	

