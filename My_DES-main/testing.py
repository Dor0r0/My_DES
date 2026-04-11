from sbox import S_BOXES


r = ['100100', '000000', '000111', '111000', '011001', '010011', '011011', '111100']
my_r = ''
for i in r:
    row = int(i[0] + i[5], 2)
    col = int(i[1:5], 2)
    my_r = ''.join([my_r, format(S_BOXES[i.index(i)][row][col], "04b")])
    print(f'this is the my_r {my_r}')
    print(f'this is the type of my_r {type(my_r)}')