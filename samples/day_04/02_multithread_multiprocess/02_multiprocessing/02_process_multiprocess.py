from multiprocessing import Pool
import time

def process(number):
    return number * 1_000_000 ** 1_000_000

if __name__ =='__main__':
    start_time = time.time()

    numbers = [(number + 1) for number in range(3)]
    with Pool() as pool:
        results = pool.map(process, numbers)

    end_time = time.time()
    print(end_time - start_time)