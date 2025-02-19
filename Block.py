from time import time
from Utility.Hasher import Hasher

class Block:
    def __init__(self,prev_hash,version):
        self.transactions=[]
        self.prev_hash=prev_hash
        self.nonce=0
        self.version=version
        self.timestamp=time()
        self.merkleroot=""
        self.blockhash=""
    
    def merkle_calculate(self):
        current_level=self.transactions
        while len(current_level)>1:
            next_level=[]
            for i in range(0,len(current_level),2):
                if i+1<len(current_level):
                    hashpair=current_level[i]['Transaction Hash'] + current_level[i+1]['Transaction Hash']
                else:
                    hashpair=current_level[i]['Transaction Hash'] + current_level[i]['Transaction Hash']
                hash=Hasher(hashpair)
                next_level.append(hash)
            current_level=next_level

        self.merkleroot=current_level[0]
    def __repr__(self):
        return f" 'Label' : 'Block' ,'Version':{Block.version},'Bock Hash':{Block.blockhash},
        'Merkle Root':{Block.merkleroot},'Time Stamp':
        {Block.timestamp},'Nonce':{Block.nonce},
        'Previous Hash':{Block.prev_hash}"
    