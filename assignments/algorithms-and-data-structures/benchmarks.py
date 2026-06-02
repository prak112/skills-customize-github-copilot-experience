import time
import random
from starter_code import merge_sort, quick_sort, binary_search


def time_func(func, *args, repeats=3):
    times = []
    for _ in range(repeats):
        t0 = time.perf_counter()
        func(*args)
        t1 = time.perf_counter()
        times.append(t1 - t0)
    return min(times)


def run():
    sizes = [100, 500, 1000]
    for n in sizes:
        arr = [random.randint(0, n) for _ in range(n)]
        s = sorted(arr)
        print(f"n={n}")
        print("merge_sort:", time_func(merge_sort, arr))
        print("quick_sort:", time_func(quick_sort, arr))
        print("binary_search (existing):", time_func(binary_search, s, s[len(s)//2]))


if __name__ == '__main__':
    run()
