from Block import Block

class Testing:
    @staticmethod
    def tester(subject):
        # for block in subject:
        #     print(block)

        for b in subject:
            # print(b.previous_hash)
            # print(b.index)
            # print([t.__dict__ for t in b.transactions])
            # print(b.proof)
            # print(b.timestamp)
            el = Block(b.previous_hash, b.index, [tx.__dict__ for tx in b.transactions], b.proof, b.timestamp)
            print(el.__dict__)
# b = Block('asnas',0,[{'sender':'a','recipient':'z','amount':10}], 107, 102993)
# b.prt()