from itertools import repeat
from multiprocessing.pool import Pool
import multiprocessing


def calcNum(a, b, c):  # some arbitrary, time-consuming calculation on a number
    print("Calcs Started on ", a, ",", b)
    aa = a
    for i in range(5000000):
        aa += i % 25
        if aa > a+b:
            aa /= 2
    return a+b


if __name__ == "__main__":
    core_nb = multiprocessing.cpu_count()
    p = Pool(processes=int(core_nb))

    nums = [1, 2, 3, 4,5,6,7,8,9,10]
    second_arg = 0

    result = p.starmap(calcNum, zip(nums, repeat(second_arg), repeat(3)))
    p.close()
    p.join()

    print(result)
