# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def write_file(file, st):
    with open(file, 'w') as data:
        data.write(st)

def read_file(file):
    with open(file, 'r') as data:
        st = data.read()
    return st

def encode(st):
    encoding = "" 
    i = 0
    while i < len(st):
        count = 1
        while i + 1 < len(st) and st[i] == st[i + 1]:
            count += 1
            i += 1
        encoding += str(count) + st[i]
        i += 1
    return encoding

def decode(st):
    decode = '' 
    count = '' 
    for i in st: 
        if i.isdigit():  
            count += i 
        else: 
            decode += i * int(count) 
            count = '' 
    return decode

s = 'ADDDDDDDDDDDDDDGGGGGGLRPPPsssssssssssss'
file_encode = 'encode.txt'
file_decode = 'decode.txt'

encode(s)
write_file(file_encode, encode(s))
decode(read_file(file_encode))
write_file(file_decode, decode(read_file(file_encode)))

print(f'исходная строка {s}')
print(f'кодированная строка {encode(s)}')
print(f'декодированная строка {decode(read_file(file_encode))}')

