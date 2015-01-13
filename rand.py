#!/usr/bin/env python3
import sys
from datetime import datetime

odds = '13579'
evens = '02468'

def generate_bit():
    now = datetime.today()
#    print('now:', now.microsecond)
    last_digit = str(now.microsecond)[-1:]
    if last_digit in odds:
        bit = '0'
    elif last_digit in evens:
        bit = '1'
    return bit

def generate_binary_string(num):
    output = ''
    for i in range(0, num):
        bit = generate_bit()
        output += bit
    return output
# ''.join(generate_bit() for _ in range(0, num)

def rand():
    num = int(sys.argv[1])
    b = generate_binary_string(num)
    print('result:', b)
    print('int:', int(b, 2))

def test():
    run = 10000
    num = int(sys.argv[1])
    count = [0 for i in range(0, num)]
    for i in range(0, run):
        b = generate_binary_string(num)
        for x in range(num):
            if b[x] == '1':
                count[x] += 1
    print(count) 

if 'test' in sys.argv:
    test()
else:
    rand()
