requests = {"Andrew": 10, "Peddy": 21, "Alex": 30, "Coney": 52}
banned = {"Alex"}

adults  = [name for name, age in requests.items() if age >= 18]
print(adults)

allowed = [name for name in adults if name not in banned]
print(allowed )