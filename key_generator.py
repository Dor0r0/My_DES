
#parity box
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

def hex_to_bin64(hex_str):
    hex_str = hex_str.removeprefix("0x").removeprefix("0X")
    return format(int(hex_str, 16), '064b')

def permute(bitstr, table):
    return ''.join(bitstr[i - 1] for i in table)

key_hex = input()
key = hex_to_bin64(key_hex)

print(key)
print(len(key))   # 64

key_56 = permute(key, PC1)
print(key_56)
print(len(key_56))  # 56

key_left = key_56[:27]
key_right = key_56[28:]

print(key_left, key_right) 