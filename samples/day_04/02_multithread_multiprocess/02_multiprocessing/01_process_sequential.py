import multiprocessing
import time


def process(number):
    return number * 1_000_000 ** 1_000_000

if __name__ =='__main__':
    start_time = time.time()

    numbers = [(number + 1) for number in range(3)]
    results = [process(number) for number in numbers]

    end_time = time.time()
    print(end_time - start_time)