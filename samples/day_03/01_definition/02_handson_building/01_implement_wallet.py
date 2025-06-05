class Wallet:

    def __init__(self, initial_amount=0):
        self.amount = initial_amount


food_wallet = Wallet(250)
transport_wallet = Wallet(1000)

print("Food Budget:", food_wallet.amount)
print("Transport Budget:", transport_wallet.amount)
