num_5 = 0b101  # 5
num_6 = 0b110  # 6

print('logical 5 AND 6: {}'.format(num_5 & num_6))
print('logical 5 OR 6: {}'.format(num_5 | num_6))
print('logical 5 XOR 6: {}'.format(num_5 ^ num_6))
print('logical NOT 5: {}'.format(~ num_5))
print('logical NOT 6: {}'.format(~ num_6))
print('bitwise right shift by two characters (for 5): {}'.format(num_5 >> 2))
print('bitwise left shift by two characters (for 5): {}'.format(num_5 << 2))
