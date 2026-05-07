from key_generator import round_keys, permute, hex_to_bin64
from pbox import IP, FP
from enc import round_function, round_function_last

print("=== DES Decryption ===")
ct_hex = input("Ciphertext (hex): ").strip()
ct_64 = hex_to_bin64(ct_hex)

# 초기 치환
current_block = permute(ct_64, IP)

# 복호화 시 키를 15번(K16)부터 1번(K2)까지 역순으로 적용
for i in range(15):
    current_block = round_function(current_block, round_keys[15 - i])

# 마지막 16번째 라운드 (K1 적용)
final_round_block = round_function_last(current_block, round_keys[0])

# 최종 치환
plaintext_bin = permute(final_round_block, FP)

print(f'64-bit plaintext (hex): {format(int(plaintext_bin, 2), "016x")}')