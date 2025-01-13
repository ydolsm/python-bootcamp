names = ['Client 1', 'Client 2', 'Client 3']
balances = [10_000, 20_000, 3_000]
ids = [1, 2, 3]

for name, balance, id in zip(names, balances, ids):
    print(f"{id}: {name} ({balance} PHP)")