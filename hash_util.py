import hashlib as hl
import json


def get_hash(block):
	"""
	This function calculates the hash of a block using SHA256 algorithm.

	Attributes:
		block: A block in a Blockchain.
	Returns:
		String format of the hashcode.
	"""
	up_block = block.__dict__.copy()
	up_block['transactions'] = [t.make_ordered() for t in up_block['transactions']]
	return hl.sha256(json.dumps(up_block,sort_keys=True).encode()).hexdigest()

def hash_str(s):
	"""
	This function calculates the hash of string using SHA256 algorithm.
	
	Attributes:
		s: string.
	Returns:
		String format of the hashcode.
	"""
	return hl.sha256(s).hexdigest()