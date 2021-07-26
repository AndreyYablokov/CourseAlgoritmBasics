num_1st_letter = ord('a')
nums_letter = 26

num = int(input('Enter a number of letter (English): '))

if 0 < num <= nums_letter:
    print('This is letter "{}"'.format(chr(num_1st_letter + num - 1)))
else:
    print('Wrong number')
