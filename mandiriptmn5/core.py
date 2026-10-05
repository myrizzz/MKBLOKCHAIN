import hashlib 
import time 
from datetime import datetime, timezone 
 
# 1. Mendefinisikan Struktur Data Tunggal (Satu Blok) 
class Block: 
    def __init__(self, index, data, prev_hash): 
        self.index = index 
        self.timestamp = time.time() 
        self.data = data 
        self.prev_hash = prev_hash 
        self.nonce = 0  # Atribut baru: angka tebakan miner
        self.hash = self.calculate_hash() 
 
    @property 
    def timestamp_readable(self): 
        local_tz = timezone.utc 
        dt = datetime.fromtimestamp(self.timestamp, tz=local_tz) 
        return dt.astimezone().strftime("%Y-%m-%d %H:%M:%S %Z") 
 
    def calculate_hash(self): 
        # Nonce ikut dimasukkan ke dalam perhitungan hash
        block_string = str(self.index) + str(self.timestamp) + str(self.data) + str(self.prev_hash) + str(self.nonce) 
        return hashlib.sha256(block_string.encode()).hexdigest() 

    def mine_block(self, difficulty): 
        # Target hash berdasarkan tingkat kesulitan
        target = "0" * difficulty 
        
        # Mencari Nonce sampai mendapatkan Hash yang sesuai target
        while self.hash[:difficulty] != target: 
            self.nonce += 1 
            self.hash = self.calculate_hash() 
        
        print(f"Block Mined! Nonce: {self.nonce} | Hash: {self.hash}")
 
# 2. Mendefinisikan Rantai Blok (Manajer Kumpulan Blok) 
class Blockchain: 
    def __init__(self): 
        self.chain = [] 
        self.difficulty = 3  # Tingkat kesulitan mining
        self.create_genesis_block() 
 
    def create_genesis_block(self): 
        # Blok pertama selalu hardcoded 
        genesis_block = Block(1, "Genesis Block (Awal Mula)", "0") 
        self.chain.append(genesis_block) 
 
    def add_block(self, data): 
        # Mengambil hash dari blok terakhir sebagai pointer 
        last_block = self.chain[-1] 
        new_block = Block(last_block.index + 1, data, last_block.hash) 
        
        # Melakukan mining sebelum blok ditambahkan ke rantai
        new_block.mine_block(self.difficulty) 
        
        self.chain.append(new_block) 
 
    def is_chain_valid(self): 
        # Loop dari blok ke-1 (setelah Genesis) sampai akhir 
        for i in range(1, len(self.chain)): 
            current_block = self.chain[i] 
            previous_block = self.chain[i-1] 
 
            # Cek apakah hash saat ini masih valid 
            if current_block.hash != current_block.calculate_hash(): 
                return False 
             
            # Cek apakah pointer prev_hash merujuk ke blok sebelumnya dengan benar 
            if current_block.prev_hash != previous_block.hash: 
                return False 
        
        return True