from key_generator import round_keys, permute, hex_to_bin64
from pbox import IP, FP
from enc import round_function, round_function_last

print("=== DES Decryption ===")
ct_hex = input("Ciphertext (hex): ").strip()
ct_64 = hex_to_bin64(ct_hex)

current_block = permute(ct_64, IP)

for i in range(15):
    current_block = round_function(current_block, round_keys[15 - i])

# 막라
final_round_block = round_function_last(current_block, round_keys[0])

# 최종 
plaintext_bin = permute(final_round_block, FP)

print(f'64-bit plaintext (hex): {format(int(plaintext_bin, 2), "016x")}')