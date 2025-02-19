import hashlib

def Hasher(data):
     # First hash: SHA-256
    sha256_hash = hashlib.sha256(data.encode()).digest()    
        # Second hash: RIPEMD-160
    ripemd160_hash = hashlib.new('ripemd160', sha256_hash).hexdigest()
    return ripemd160_hash