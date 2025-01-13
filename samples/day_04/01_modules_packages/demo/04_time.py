import time

# Current time
print("Current Time:")
print(time.ctime())
print()

# Measuring execution time
print("Measuring Execution Time:")
start_time = time.time()
for i in range(1_000_000):
    x = 10 ** 1000
end_time = time.time()
print(f"Loop execution time: {end_time - start_time:.5f} seconds")
print()

# Sleep function
print("Using Sleep:")
print("Waiting for 2 seconds...")
time.sleep(10)
print("Done!")
