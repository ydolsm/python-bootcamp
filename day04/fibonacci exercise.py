from multiprocessing import Pool
import time

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ =="__main__":
    start_time = time.time()
    numbers = [35, 36, 37, 38]

    with Pool() as pool:
        result = pool.map(fibonacci, numbers)
        print(f"Fibonacci({numbers}) = {result}")

    end_time = time.time()
    print(end_time - start_time)