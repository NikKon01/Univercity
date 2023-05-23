import time

def time_it(func):
    to = time.time()
    res = func(1000000)
    t = time.time()
    print(f"Время работы функции {func.__name__}: {t - to}")
    return res


@time_it
def chet_numbers_append(n):
    chet_list = []
    for i in range(n + 1):
        if i % 2 == 0:
            chet_list.append(i)
    return chet_list


@time_it
def chet_numbers_comprehension(n):
    chet_list = [i for i in range(n + 1) if i % 2 == 0]
    return chet_list