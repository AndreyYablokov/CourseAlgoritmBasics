# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как
# массив, элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’,
# ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’,
# ‘E’]

class HexNumbers:
    dec_nums = [num for num in range(16)]
    hex_nums = [str(num) for num in range(10)] + ['a', 'b', 'c', 'd', 'e', 'f']
    dict_hex = {}
    dict_dec = {}
    for hex_num, dec_num in zip(hex_nums, dec_nums):
        dict_hex[hex_num] = dec_num
        dict_dec[dec_num] = hex_num

    mul_table = [[hex(num * prod)[2:] for num in range(16)] for prod in range(16)]

    def __init__(self, hex_number_str):
        for letter in hex_number_str:
            if letter not in HexNumbers.hex_nums:
                raise ValueError('This is not hexadecimal number')
        self._hex_number = list(hex_number_str.lower())

    @property
    def hex_number(self):
        return self._hex_number.copy()

    def __str__(self):
        return ''.join(self._hex_number)

    def __add__(self, other):
        num_1 = self.hex_number
        num_2 = other.hex_number
        num_1.reverse()
        num_2.reverse()
        result = []
        additive = 0
        idx = 0
        for digit_1_str, digit_2_str in zip(num_1, num_2):
            digit_1_dec = HexNumbers.dict_hex[digit_1_str]
            digit_2_dec = HexNumbers.dict_hex[digit_2_str]
            sum_digits = digit_1_dec + digit_2_dec + additive
            if sum_digits > 15:
                additive = 1
                result.append(HexNumbers.dict_dec[sum_digits - 16])
            else:
                additive = 0
                result.append(HexNumbers.dict_dec[sum_digits])
            idx += 1

        if len(num_1) < len(num_2):
            num_1, num_2 = num_2, num_1
        if len(num_1) != len(num_2):
            for digit_dec in num_1[idx::]:
                sum_digits = HexNumbers.dict_hex[digit_dec] + additive
                if sum_digits > 15:
                    additive = 1
                    result.append(HexNumbers.dict_dec[sum_digits - 16])
                else:
                    additive = 0
                    result.append(HexNumbers.dict_dec[sum_digits])

        if additive == 1:
            result.append('1')

        result.reverse()

        return self.__class__(''.join(result))

    @staticmethod
    def _product_one_digit(num, factor):
        number = num.copy()
        number.reverse()
        dim1 = HexNumbers.hex_nums.index(factor)
        result = HexNumbers('0')
        for idx, digit in enumerate(number):
            dim2 = HexNumbers.hex_nums.index(digit)
            result += HexNumbers(f'{HexNumbers.mul_table[dim1][dim2]}{"0" * idx}')

        return result

    def __mul__(self, other):
        result = HexNumbers('0')
        num_1 = self.hex_number
        num_2 = other.hex_number
        num_2.reverse()
        for idx, num_2_digit in enumerate(num_2):
            prom_res = f'{HexNumbers._product_one_digit(num_1.copy(), num_2_digit).__str__()}{"0" * idx}'
            result += HexNumbers(prom_res)

        return result


if __name__ == '__main__':
    num_1_hex_str = input('Enter the first hexadecimal number: ')
    num_2_hex_str = input('Enter the second hexadecimal number: ')
    num_1_hex = HexNumbers(num_1_hex_str)
    num_2_hex = HexNumbers(num_2_hex_str)
    sum_hex_num = num_1_hex + num_2_hex
    prod_hex_num = num_1_hex * num_2_hex
    print(f'Result of sum: {sum_hex_num}')
    print(f'Result of product: {prod_hex_num}')
