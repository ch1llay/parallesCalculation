import multiprocessing

import time

def worker(x):
    name_proc = multiprocessing.current_process().name
    res = x*x
    # print(name_proc, res)
    return res

data = range(100000000)


if __name__ == "__main__":
    with multiprocessing.Pool(20) as pool:
        print('Результаты:')
        t = time.time()
        l = list(pool.map(worker, data))
        print("готово")
        print(time.time() - t)
        # print(l)
