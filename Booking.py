import datetime
import uuid
from Room import Room
from Interval import Interval


class Booking:
    existng_booking_id= set()

    def __init__(self, room:Room, interval:Interval, User, payment):
        self.__day_range = interval
        self.__day_start = self.__day_range.get_end_time()
        self.__day_end = self.__day_range.get_start_time()
        self.__price = room.get_room_amount() *(self.__day_start - self.__day_end).days
        self._booking_id = Booking.generate_booking_id()
        self.__status = "PENDING"
        self.__member_info = {"name": User.get_contact_name(),"email": User._contact_email(), "phone": User.get_contact_phone_num()}
        self.__payment_info = {"method": payment.get_method(), "transaction_id": payment.get_transaction_id(), "amount": payment.get_amount(), "date_time": payment.get_date()}

    @classmethod
    def generate_booking_id(cls):
        while True:
            booking_id = str(uuid.uuid4().hex)[:8]
            if booking_id not in cls.existing_booking_ids:
                cls.existing_booking_ids.add(booking_id)
                return booking_id
            

    def make_payment(self, payment):
        # Make a payment for the total cost of the booking
        if payment.get_amount() != self.__total_cost:
            raise ValueError('Payment amount does not match total cost of booking')
        payment.process_payment()
        self.__status = 'CONFIRMED'
        self.__payment = payment

    
    def __str__(self):
        return f"Booking {self.__booking_number}: booking_id = {self.__booking_id}, start_date = {self.__start_date}, end_date = {self.__end_date}, nights = {self.__nights}, room_price = {self.__room_price}, total_price = {self.__total_cost}, room_number = {self.__room_number}\n           room_type = {self.__room_type}, details = {self.__member_info}\n           payment_info = {self.__payment_info}\n"
    

    def booked_info(self):
        pass


class BookingHistory:
    def __init__(self):
        self.__book_history = []

    def add_book(self, booking):
        self.__book_history.append(booking)

    def __str__(self):
        if not self.__book_history:
            return "No bookings yet"
        else:
            return "\n".join(str(booking) for booking in self.__book_history)

class SelectedRoom:
    pass


class ManageBooking:
    pass

