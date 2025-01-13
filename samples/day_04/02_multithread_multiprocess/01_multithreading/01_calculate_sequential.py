import concurrent.futures
import time

def process(number):
    _ = number * 1_000_000 ** 1_000_000
    print("Finished computation")

if __name__ =='__main__':
    start_time = time.time()

    user_input = input("Enter number: ")

    print("Start calculating")
    process(3)

    end_time = time.time()
    print(end_time - start_time)