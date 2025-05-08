"""
Lösung über abstrakte Klassen und Dependency Injection
"""

from abc import ABC, abstractmethod


class PaymentGateway(ABC):

    @abstractmethod
    def process_payment(self, amount): ...


class PaypalGateway(PaymentGateway):
    def process_payment(self, amount):
        print("Processing Paypal Transaction")


class StripeGateway(PaymentGateway):
    def process_payment(self, amount):
        print("Processing Stripe Transaction")


class PaymentProcessor:
    def __init__(self, payment_gateway: PaymentGateway):
        self.payment_gateway = payment_gateway

    def make_payment(self, amount: float):
        print("Payment processing initiated")
        self.payment_gateway.process_payment(amount)
        print("Payment processing completed")


if __name__ == "__main__":
    paypal = PaypalGateway()
    payment_processor = PaymentProcessor(paypal)
    payment_processor.make_payment(100.0)
