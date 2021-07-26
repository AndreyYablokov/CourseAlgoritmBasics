year = int(input('Enter year: '))

if year % 4 != 0:
    print('This is not a leap year')
elif year % 100 != 0:
    print('This is not a leap year')
elif year % 400 != 0:
    print('This is not a leap year')
else:
    print('This is leap year')
