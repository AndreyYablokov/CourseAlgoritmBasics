num_1st_letter = ord('a')

letter_1, letter_2 = input('Enter the letters separated by space: ').split()

num_letter_1 = ord(letter_1)
num_letter_2 = ord(letter_2)
if num_letter_1 == num_letter_2:
    num_letter_between = 0
else:
    num_letter_between = abs(num_letter_1 - num_letter_2) - 1

print('Number of first letter {} is {}'.format(letter_1, num_letter_1-num_1st_letter+1))
print('Number of second letter {} is {}'.format(letter_2, num_letter_2-num_1st_letter+1))
print(f'Numbers of letters between {letter_1} an {letter_2} is {num_letter_between}')
