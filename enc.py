from key_generator import round_keys
from pbox import *


def permute(bitstr, table):
    return ''.join(bitstr[i - 1] for i in table)

def hex_to_bin64(hex_str):
    hex_str = hex_str.removeprefix("0x").removeprefix("0X")
    return format(int(hex_str, 16), '064b')

block_hex = input().strip()
block_64 = hex_to_bin64(block_hex)
ip_block = permute(block_64, IP)

print(ip_block)