from abc import ABC, abstractmethod

class PaymentMethod:
    @abstractmethod
    def pay(self, amount: int):
        'Abstract method for payment'
        pass

class CreditCardPayment(PaymentMethod):
    def pay(self, amount: int):
        'Implementation of credit card payement method'
        print(f'Paying ${amount} using credit card...')


class BitCoinPayment(PaymentMethod):
    def pay(self, amount: int):
        'Implementation of credit card payement method'
        print(f'Paying ${amount} using bitcoin...')

class ShoppingCart:
    def __init__(self, payment_method: PaymentMethod):
        self.payment_method = payment_method
    
    def checkout(self, amount):
        self.payment_method.pay(amount)


if __name__ == '__main__':
    cart = ShoppingCart(BitCoinPayment())
    amount = 10
    cart.checkout(amount)