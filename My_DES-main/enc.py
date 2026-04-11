from key_generator import round_keys,permute,hex_to_bin64
from pbox import IP,FP
from sbox import S_BOXES


expansion_p_list =[32, 1, 2, 3, 4, 5, 4, 5, 6, 7,
                    8, 9, 8, 9, 10, 11, 12, 13, 12, 
                    13, 14, 15, 16, 17, 16, 17, 18, 
                    19, 20, 21, 20, 21, 22, 23, 24, 
                    25, 24, 25, 26, 27, 28, 29, 28, 
                    29, 30, 31, 32, 1]

straight_p_list = [16, 7, 20, 21, 29, 12, 28, 17,
                    1, 15, 23, 26, 5, 18, 31, 10,
                    2, 8, 24, 14, 32, 27, 3, 9,
                    19, 13, 30, 6, 22, 11, 4, 25]


def des_function(r, k):   
    r = bit_xor(permute(r, expansion_p_list), k)
    r = [r[i:i+6] for i in range(0, len(r), 6)]
    my_r = ''
    for i in r:
        row = int(i[0] + i[5], 2)
        col = int(i[1:5], 2)
        my_r = ''.join([my_r, format(S_BOXES[i.index(i)][row][col], "04b")])
    my_r = permute(my_r, straight_p_list)
    return my_r

def bit_xor(a, b):
    return ''.join('1' if x != y else '0' for x, y in zip(a, b))

def round_function(i, k): 
    initial_left = i[:32]
    initial_right = i[32:]
    mixer_round = initial_left + des_function(initial_right, k)  
    mixer_round_left = mixer_round[:32]
    mixer_round_right = mixer_round[32:]
    swapper_round = mixer_round_right + mixer_round_left
    print(f'this is the mixer_round {mixer_round}')
    return swapper_round

def round_function_last(i, k):
    initial_left = i[:32]
    initial_right = i[32:]
    mixer_round = initial_left + des_function(initial_right, k)
    print(f'this is the mixer_round {mixer_round}')
    return mixer_round





pt_hex = input().strip()
pt_64 = hex_to_bin64(pt_hex)
ip_block = permute(pt_64, IP)

i = 0
while i < 15:
    ip_block = round_function(ip_block, round_keys[i])  #오류
    i += 1
round16 = round_function_last(ip_block, round_keys[15])
op_block = permute(round16, FP)

print(f'64-bit plaintext: {op_block}')
print(f'64-bit ciphertext: {pt_64}')
print(f'64-bit ciphertext (hex): {format(int(op_block, 2), "016x")}')