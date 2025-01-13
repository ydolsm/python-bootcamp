import os
import time

# Current working directory
print("Current Working Directory:")
print(os.getcwd())
print()

# List directory contents
print("Listing Directory Contents:")
for item in os.listdir(""):
    print(item)
print()

# Create and remove a directory
print("Creating and Removing a Directory:")
os.mkdir("demo_dir")

print(f"Directory 'demo_dir' created.")
os.rmdir("demo_dir")
print(f"Directory 'demo_dir' removed.")
