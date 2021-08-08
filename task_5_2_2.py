def hex_to_dec(number_hex):
    dec_nums = [num for num in range(16)]
    hex_nums = [str(num) for num in range(10)] + ['a', 'b', 'c', 'd', 'e', 'f']
    dict_hex = {}
    for key, value in zip(hex_nums, dec_nums):
        dict_hex[key] = value

    number_hex.reverse()
    number_dec = 0
    for idx, digit in enumerate(number_hex):
        number_dec += dict_hex[digit] * pow(16, idx)

    return number_dec


def dec_to_hex(number_dec):
    dec_nums = [num for num in range(16)]
    hex_nums = [str(num) for num in range(10)] + ['a', 'b', 'c', 'd', 'e', 'f']
    dict_dec = {}
    for key, value in zip(dec_nums, hex_nums):
        dict_dec[key] = value

    number_hex = []
    while number_dec > 16:
        number_hex.append(dict_dec[number_dec % 16])
        number_dec //= 16
    number_hex.append(dict_dec[number_dec])

    number_hex.reverse()

    return number_hex


if __name__ == '__main__':
    num_1_hex = list(input('Enter the first hexadecimal number: ').lower())
    num_2_hex = list(input('Enter the second hexadecimal number: ').lower())
    num_1_dec = hex_to_dec(num_1_hex)
    num_2_dec = hex_to_dec(num_2_hex)

    sum_nums_dec = num_1_dec + num_2_dec
    prod_nums_dec = num_1_dec * num_2_dec

    sum_nums_hex = dec_to_hex(sum_nums_dec)
    prod_nums_hex = dec_to_hex(prod_nums_dec)

    print('Sum of numbers: {}'.format("".join(sum_nums_hex)))
    print('Product of numbers: {}'.format("".join(prod_nums_hex)))
