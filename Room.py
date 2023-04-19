class Room:
    def __init__(self, hotel_name, room_number, room_name, room_area, number_bedroom, number_bathroom, date_not_available, room_amount):
        self._hotel_name = hotel_name
        self.room_number = room_number
        self._room_name = room_name
        self._room_area = room_area
        self._number_of_bathroom = number_bedroom
        self._number_of_bedroom = number_bathroom
        self._date_not_available = []
        self._room_amount = room_amount
        self._status_available = True

    # def add_interval(self, interval):
    #     self._date_not_available.append(interval)

    # def check_no_overlap(self,start_time1, end_time1, start_time2, end_time2):
    #     if start_time1 > end_time2 or start_time2 > end_time1:
    #         return True
    #     else:
    #         return False

    # def room_available(self, datetime1, datetime2):
    #     for i in self._date_not_available:
    #         if not self.check_no_overlap(i.get_start_time(), i.get_end_time(), datetime1, datetime2):
    #             return False
    #     return True
    
    def get_room_area(self):
         return self._room_area
    
    def get_room_number(self):
        return self._room_number

    def get_hotel_name(self):
        return self._hotel_name
    
    def get_room_name(self):
        return self._room_name
    
    def get_date_not_avalible(self):
        return self._date_not_available

    def get_status_available(self):
        return self._status_available
    
    
    def get_room_amount(self):
        return self._room_amount
          
    def add_interval(self,interval):
        self._date_not_available.append(interval)

    def check_no_overlap(self,start_time1, end_time1, start_time2, end_time2):
        if start_time1 > end_time2 or start_time2 > end_time1:
            return True
        else:
            return False

    def room_available(self, datetime1, datetime2):
        for i in self._date_not_available:
            if not self.check_no_overlap(i.get_start_time(), i.get_end_time(), datetime1, datetime2):
                return False
        return True
        
