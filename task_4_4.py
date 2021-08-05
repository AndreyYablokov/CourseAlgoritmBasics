# Алгоритм вычисления чисел Фибоначчи

import cProfile


def f(n):
    if n < 2:
        return n
    pp = 0
    p = 1
    for i in range(n - 1):
        pp, p = p, pp + p
    return p


if __name__ == '__main__':
    cProfile.run('f(100)')
    cProfile.run('f(200)')
    cProfile.run('f(250)')
    cProfile.run('f(255)')
    cProfile.run('f(256)')
    cProfile.run('f(300)')
    cProfile.run('f(400)')
    cProfile.run('f(500)')
    cProfile.run('f(1000)')
    cProfile.run('f(10000)')
    cProfile.run('f(100000)')
    cProfile.run('f(1000000)')

# Для n = 100-1000 -> 0.000 s
# Для n = 10000 -> 0.003 s
# Для n = 100000 -> 0.103 s
# Для n = 1000000 -> 8.251 s
