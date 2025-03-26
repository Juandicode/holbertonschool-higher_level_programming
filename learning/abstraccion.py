from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount}")

class PayPalPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}")

# Test
credit_card = CreditCardPayment()
paypal = PayPalPayment()

credit_card.process_payment(100)  # Output: Processing credit card payment of $100
paypal.process_payment(50)       # Output: Processing PayPal payment of $50