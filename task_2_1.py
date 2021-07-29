# The calculator program

print('The calculator program. Example of entering an expression: 2 + 2. Valid characters: +, -,*,/. To exit, enter 0')
while True:
    user_expression = input('Enter the expression to calculate: ')
    if user_expression == '0':
        break
    try:
        num_1, operation, num_2 = user_expression.split()
        num_1 = float(num_1)
        num_2 = float(num_2)
        if operation == '+':
            print('Result: {}'.format(num_1 + num_2))
        elif operation == '-':
            print('Result: {}'.format(num_1 - num_2))
        elif operation == '*':
            print('Result: {}'.format(num_1 * num_2))
        elif operation == '/':
            print('Result: {}'.format(num_1 / num_2))
        else:
            print('Invalid operation')
    except ZeroDivisionError:
        print('Division by zero is not possible')
    except ValueError:
        print('Error in the expression')
