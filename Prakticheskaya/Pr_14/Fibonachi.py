import time

def time_it(fn):
    def wrapper(*args):
        to = time.time()
        fn(*args)
        t = time.time() - to
        print(f"Время работы: {t} сек")

    return wrapper

def fibonachi_cache(fn):
    cache = {}

    def wrapper(n):

        if n in cache:
            return cache[n]

        if not cache:
            for i in range(min(2, n + 1)):
                cache[i] = i

        for i in range(len(cache), n + 1):
            cache[i] = cache[i-1] + cache[i-2]

        print(f"last cached number is {cache[n]}")
        return cache[n]

    return wrapper

@time_it
@fibonachi_cache
def fibonachi(n):
    return n if n == 0 or n == 1 else fibonachi(n - 1) + fibonachi(n - 2)

n = int(input("Введите число: "))
no = int(input("Введите то же число: "))
n2 = int(input("Введите новое число побольше: "))

print("  ===========")
print(fibonachi(n))
print("  ===========")
print(fibonachi(no))
print("  ===========")
print(fibonachi(n2))