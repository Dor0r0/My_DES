from key_generator import round_keys,permute,hex_to_bin64
from pbox import *



block_hex = input().strip()
block_64 = hex_to_bin64(block_hex)
ip_block = permute(block_64, IP)

print(ip_block)