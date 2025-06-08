class Payment:
    def __init__(self, initial_amount=0):
        self.amount = initial_amount

    def valid(self):
        return self.amount >= 0

class Coupon(Payment):
    def __init__(self, amount, expired):
        super().__init__(amount)
        self.expired = expired

    def valid(self):
        return super().valid() and not self.expired

class CardPayment(Payment):
    def __init__(self, amount, card_number):
        super().__init__(amount)
        self.card_number = card_number

    def valid(self):
        #allnumeric = self.card_number.isnumeric()
        return super().valid() and len(self.card_number) == 16 and self.card_number.isnumeric()

class OnlinePayment(Payment):
    def __init__(self, amount, email):
        super().__init__(amount)
        self.email = email

    def valid(self):
        return super().valid() and self.email.endswith("@gmail.com")

#print coupon payment
coupon_payment = Coupon(4000, "False")
print(f"Coupon payment amount:", coupon_payment.amount)

#print card payment
card_payment = CardPayment(1000, "4126745974513584")
print (f"Card payment amount:", card_payment.amount)

#print online payment
online_payment = OnlinePayment(5000, "4126745974513584")
print (f"Online payment amount:", online_payment.amount)
