from Room import Room
from datetime import datetime
from Interval import Interval
from Booking import Booking
class RoomCatalog:

    def __init__(self):
        self._room_lists = []
        self._check = True

    def add_room(self,room):
        self._room_lists.append(room)

    def show_catalog(self):
        for i in self._room_lists:
            print(i._room_name)
            
        
    def search_car_by_brand(self, search_string):
        self.__list_of_car = []
        for obj in self._car_lists:
            if search_string.lower() in obj.get_car_brand().lower():
                self.__list_of_car.append(obj)
        return self.__list_of_car
    

     
    def find_available_room(self, start_date, start_time, end_date, end_time):
        date1 = datetime.strptime(start_date + " " + start_time, '%d-%m-%Y %H:%M')
        date2 = datetime.strptime(end_date + " " + end_time, '%d-%m-%Y %H:%M')
        available_room = []
        for i in self._room_lists:
            if not i.get_status_available():
                continue
            if not i.room_available(date1, date2):
                continue
            available_room.append(i)
        return available_room
    
    def book_room(self,cars,start_date,start_time,end_date,end_time):
        for i in self._room_lists:
            if i.get_car_plate_number()== cars:
                book_car = i
                break

        interval = Interval(start_date,start_time,end_date,end_time)
        booking = Booking(book_car,interval)
        return booking
    

    

            
    