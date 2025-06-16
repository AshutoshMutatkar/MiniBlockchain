#MiniBlockchain
import hashlib
import datetime
class Block: 
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = str(self.index)+ str(self.timestamp)+ str(self.data)+ str(self.previous_hash)
        return hashlib.sha256(block_string.encode()).hexdigest()
    
class Blockchain: 
    def __init__(self):
        self.chain =[self.create_genesis_block()]
# Create Genesis Block 
    def create_genesis_block(self):
        return Block(0,str(datetime.datetime.now()), "Genesis Block", "0")
 # Get the latest block   
    def get_latest_block(self):
        return self.chain[-1]
 # add a new block   
    def add_block(self, new_data):
        latest_block = self.get_latest_block()
        new_block = Block(len(self.chain), str(datetime.datetime.now()), new_data,latest_block.hash)
        self.chain.append(new_block)

# testing the blockchain
if __name__=="__main__":
# initialize blockchain
    my_blockchain = Blockchain()
# add some blocks
    my_blockchain.add_block("Messi sends 5 coins to Suarez")   #messi = person a; suarez = person b;neymar = person c
    my_blockchain.add_block("Suarez sends 2 coins to Neymar")    
# print the blockchain
    for block in my_blockchain.chain:
        print("Block Index:", block.index)
        print("Timestamp: ", block.timestamp) 
        print("Data: ", block.data)
        print("Previous Hash: ", block.previous_hash)
        print("Hash: ",block.hash)
        print("-" * 50)