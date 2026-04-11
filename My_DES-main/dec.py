from enc import *



print("=== DES Decryption ===")
pt_hex = input().strip()
pt_64 = hex_to_bin64(pt_hex)
ip_block = permute(pt_64, IP)

i = 0
while i < 15:
    ip_block = round_function(ip_block, round_keys[15 - i])
    i += 1
round16 = round_function_last(ip_block, round_keys[0])
op_block = permute(round16, FP)

print(f'64-bit ciphertext: {op_block}')
print(f'64-bit plaintext: {pt_64}')
print(f'64-bit ciphertext (hex): {format(int(op_block, 2), "016x")}')
