from key_generator import round_keys, permute, hex_to_bin64
from pbox import IP, FP
from sbox import S_BOXES

expansion_p_list = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7,
                    8, 9, 8, 9, 10, 11, 12, 13, 12, 
                    13, 14, 15, 16, 17, 16, 17, 18, 
                    19, 20, 21, 20, 21, 22, 23, 24, 
                    25, 24, 25, 26, 27, 28, 29, 28, 
                    29, 30, 31, 32, 1]

straight_p_list = [16, 7, 20, 21, 29, 12, 28, 17,
                    1, 15, 23, 26, 5, 18, 31, 10,
                    2, 8, 24, 14, 32, 27, 3, 9,
                    19, 13, 30, 6, 22, 11, 4, 25]

def bit_xor(a, b):
    return ''.join('1' if x != y else '0' for x, y in zip(a, b))

def des_function(r, k):   
    expanded_r = permute(r, expansion_p_list)
    xored = bit_xor(expanded_r, k)
    chunks = [xored[i:i+6] for i in range(0, len(xored), 6)]
    
    my_r = ''
    for idx, chunk in enumerate(chunks):
        row = int(chunk[0] + chunk[5], 2)
        col = int(chunk[1:5], 2)
        # i.index(i) 대신 enumerate의 idx를 사용해야 각기 다른 S-Box를 참조함
        val = S_BOXES[idx][row][col]
        my_r += format(val, "04b")
        
    my_r = permute(my_r, straight_p_list)
    return my_r

def round_function(i, k): 
    left = i[:32]
    right = i[32:]
    # DES Standard: 다음 L = 현재 R, 다음 R = 현재 L XOR f(R, K)
    new_left = right
    new_right = bit_xor(left, des_function(right, k))
    return new_left + new_right

def round_function_last(i, k):
    left = i[:32]
    right = i[32:]
    # 마지막 라운드는 좌우를 바꾸지 않음 (교과서적 구현 혹은 복호화 직전 처리)
    new_left = bit_xor(left, des_function(right, k))
    new_right = right
    return new_left + new_right

if __name__ == "__main__":
    print("=== DES Encryption ===")
    pt_hex = input("Plaintext (hex): ").strip()
    pt_64 = hex_to_bin64(pt_hex)
    
    current_block = permute(pt_64, IP)

    for i in range(15):
        current_block = round_function(current_block, round_keys[i])
    
    # 16라운드
    final_round_block = round_function_last(current_block, round_keys[15])
    ciphertext = permute(final_round_block, FP)

    print(f'64-bit ciphertext (hex): {format(int(ciphertext, 2), "016x")}')