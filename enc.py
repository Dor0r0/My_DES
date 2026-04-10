from key_generator import round_keys,permute,hex_to_bin64
from pbox import IP,FP



pt_hex = input().strip()
pt_64 = hex_to_bin64(pt_hex)
ip_block = permute(pt_64, IP)

print(ip_block)