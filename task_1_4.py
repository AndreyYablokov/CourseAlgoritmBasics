import random

type_gen = int(input('What do you want to generate? (1 - integer; 2 - float; 3 - letter): '))
left_boundary, right_boundary = input('Enter a range (values must be separated by space): ').split()
if type_gen == 1:
    print('Result: {}'.format(random.randint(int(left_boundary), int(right_boundary))))
elif type_gen == 2:
    print('Result: {}'.format(random.uniform(float(left_boundary), float(right_boundary))))
elif type_gen == 3:
    num_left_letter = ord(left_boundary)
    num_right_letter = ord(right_boundary)
    if ord('a') <= num_left_letter <= ord('z') and ord('a') <= num_right_letter <= ord('z'):
        print('Result: {}'.format(chr(random.randint(num_left_letter, num_right_letter))))
    else:
        print('Wrong range')
