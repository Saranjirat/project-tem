import uuid
import time

class Payment:
    def __init__(self, member, amount, method):
        self.__member = member
        self.__amount = amount
        self.__method = method
        self.__status = 'PENDING'
        self.__date = time.ctime()
        self.__transaction_id = None

    def process_payment(self):
        # Process the payment using the specified payment method
        # This might involve communicating with a payment gateway or other payment processing service
        # Once the payment has been processed, update the status of the Payment object to "Paid"
        self.__transaction_id = str(uuid.uuid4())
        self.__status = 'Paid'
        print(f'Payment of {self.__amount} using {self.__method} processed successfully.')
    
    def get_status(self):
        return self.__status
    
    def set_status(self, status):
        self.__status = status
        return self.__status
    
    def get_amount(self):
        return self.__amount
    
    def get_method(self):
        return self.__method
    
    def get_transaction_id(self):
        return self.__transaction_id
    
    def get_date(self):
        return self.__date

class CreditPayment(Payment):
    def __init__(self, member, amount, card_number, cardholder_name, expiration_date,):
        super().__init__(member, amount, method="Credit")
        self.__card_number = card_number
        self.__cardholder_name = cardholder_name
        self.__expiration_date = expiration_date
    
    def insert_card():
        pass