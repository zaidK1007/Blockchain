from blockchain import Blockchain
from Verification import Verifier
import sys
class Node:
    """
    This class manages the Interface for the user of the Blockchain.
    Attributes:
        user: The user of the Blockchain.
        blockchain: Instance of the class Blockchain
    """
    def __init__(self, user):
        """
		This function initialise the node.

		Attributes:
		user: Name of the user
		"""
        self.user = user
        self.blockchain = Blockchain(self.user)
        if not Verifier().is_valid(self.blockchain.get_chain()):
            print('Invalid Blockchain')
            sys.exit()

    def get_user_input(self):
        """
        This function takes input from the user.

        Returns:
            The recipient and amount that is entered.
        """
        rec = input('Enter recipient: ')
        amt = float(input('Enter Amount: '))
        return rec,amt

    def print_blockchain(self):
        """
        This function prints the Blockchain.
        """
        for block in self.blockchain.get_chain():
            print('-'*15)
            print(block)
            print('-'*15)

    def execute(self):
        """
        This function starts the execution of the interface.
        """
        run = True
        while run:
            print('*'*15)
            
            print('1.Add transactions')
            print('2.Mine Block')
            print('3.Print Blockchain')
            print('Q.Quit')
            print('*'*15)

            user_choice = input('Enter your choice: ')
            if user_choice == '1':
                recipient, amount = self.get_user_input()
                if self.blockchain.add_transaction(recipient, amount, sender = self.user):
                    print('Transaction Successful')
                else:
                    print('Transaction Failed: Insufficient Balance')
            elif user_choice == '2':
                self.blockchain.mine_block()
            elif user_choice == '3':
                self.print_blockchain()
            
            elif user_choice == 'q' or user_choice == 'Q':
                run = False
            else:
                print('Invalid input')

            if not Verifier().is_valid(self.blockchain.get_chain()):
                print('Invalid Blockchain')
                break 
            coins = self.blockchain.get_balance(self.user)
            print('Balance of {0} : {1} coins'.format(self.user,coins))

node = Node('Zaid')
node.execute()