from Utility.Hasher import Hasher
import socket
import threading
yournode="Node1"


def mine(Block,difficulty=4):
    stop_mining=False

    def recieve_block():
        '''Recieve block as a nested consensus function in itself, as when we
        recieve a block, we will check if it is valid or not'''
        
        def consensus(Block):
            '''Consensus, to check if the block is valid and if it is, then stop mining'''           
            global stop_mining
            blockhash=Hasher(str(Block.timestamp) + str(Block.merkleroot) + str(Block.prev_hash)
                                    + str(Block.nonce) + str(Block.version))
            if blockhash==Block.blockhash:
                '''Call Block Adder Function'''
                stop_mining=True
                return True
            else:
                pass
    
        '''This is the code for recieving through all channels'''
        global stop_mining
        host = "0.0.0.0"  # Listen on all interfaces
        port = 12345

        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((host, port))
        server_socket.listen(5)  # Allow up to 5 pending connections

        print(f"Server listening on {host}:{port}")
        #Here if it is a transaction, we need to call its module
        conn, addr = server_socket.accept()    
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"Received from {addr}: {data.decode()}")
            consensus(data)       
        
        
    '''Now begins the Mining Code, initially we create a thread to check for messages parallely as we mine'''
    threading.Thread(target=recieve_block).start()
    while not stop_mining:
        blockhash = Hasher(str(Block.timestamp) + str(Block.merkleroot) + str(Block.prev_hash)
                           + str(Block.nonce) + str(Block.version))
        if blockhash[:difficulty] == "0" * difficulty:
            print(f"Block Mined! Nonce: {Block.nonce}, Hash: {Block.blockhash}")
            break

        Block.nonce += 1
        print(f"Mining Block : {Block.version} for Nonce Value: {Block.nonce}", end="\r")



    
