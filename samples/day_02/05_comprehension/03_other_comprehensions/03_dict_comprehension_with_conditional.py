example = {
    f"Key {num}": f"Value {num}"
    for num in range(3)
    if num != 0
}

print(example)