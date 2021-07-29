def show_symbols_ascii(start_num, finish_num):
    """Displays ascii table characters"""
    print('-'*90)
    for idx, sym_num in enumerate(range(start_num, finish_num + 1)):
        if idx % 9 == 0 and idx != 0:
            print('\n')
        print(f'{sym_num:3d} - {chr(sym_num)} ', end='| ')
    print('\n', '-' * 90)


if __name__ == '__main__':
    show_symbols_ascii(32, 127)
