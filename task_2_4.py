def sum_alternating_series(count_elems):
    """Returns the sum of the series: 1 -1/2 1/4 -1/8 ..."""
    sum_elems = 0
    for idx in range(count_elems):
        elem = ((-1)**idx)*(1/(2**idx))
        print(elem, end=' ')
        sum_elems += elem
    return sum_elems


if __name__ == '__main__':
    count_elements = int(input('Enter a count elements of series: '))
    print(f'\nSum of elements: {sum_alternating_series(count_elements)}')
