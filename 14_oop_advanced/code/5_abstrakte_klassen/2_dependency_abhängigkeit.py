"""
Payment Processor hat eine Abhängigkeit auf PaypalGate
Wie kann man das besser machen?

"""


class PayPalGateway:
    def process_payment(self, amount):
        print(f"Processing payment of ${amount} via PayPal")


class PaymentProcessor:
    def __init__(self):
        self.payment_gateway = PayPalGateway()  # Abhängigkeit

    def make_payment(self, amount):
        print("Payment processing initiated")
        self.payment_gateway.process_payment(amount)
        print("Payment processing completed")


# Client code
if __name__ == "__main__":
    payment_processor = PaymentProcessor()
    payment_processor.make_payment(100.0)
