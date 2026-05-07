PC1 = [
    57, 49, 41, 33, 25, 17, 9,
    1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27,
    19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29,
    21, 13, 5, 28, 20, 12, 4
]

PC2 = [
    14, 17, 11, 24,  1,  5,  3, 28,
    15,  6, 21, 10, 23, 19, 12,  4,
    26,  8, 16,  7, 27, 20, 13,  2,
    41, 52, 31, 37, 47, 55, 30, 40,
    51, 45, 33, 48, 44, 49, 39, 56,
    34, 53, 46, 42, 50, 36, 29, 32
]




SHIFTS = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]


def hex_to_bin64(hex_str):
    hex_str = hex_str.removeprefix("0x").removeprefix("0X")
    return format(int(hex_str, 16), '064b').zfill(64) 

def permute(bitstr, table):
    return ''.join(bitstr[i - 1] for i in table)

def left_rotate(bits, n):
    return bits[n:] + bits[:n]

def generate_round_keys(key64):
    keys = []
    key56 = permute(key64, PC1)
    c = key56[:28]
    d = key56[28:]
    for s in SHIFTS:
        c = left_rotate(c, s)
        d = left_rotate(d, s)
        keys.append(permute(c + d, PC2))
    return keys

key_hex = input("Enter 64-bit Key (hex): ").strip()
round_keys = generate_round_keys(hex_to_bin64(key_hex))