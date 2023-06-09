from Room import *
from datetime import *
from fastapi import FastAPI
from dto import *
import random
from account import*
from CreditCard import*
from Interval import*
from RoomCatalog import*
from Payment import *
from System import *
app = FastAPI()

room_plantationview = Room("Kirimayaresort",
                           "1001",
                           "Plantation View",
                           "42 sq. m.",
                           "1 Bedroom",
                           "1 Room",
                           [],
                           "1000")
                

room_horizonview = Room("Kirimayaresort",
                        "1002",
                        "Horizon View",
                        "42 sq. m.",
                        "1 Bedroom",
                        "1 Room",
                        [],
                        "2000")

room_terrace_suite = Room("Kirimayaresort",
                          "1003",
                          "Terrace Suite",
                          "84 sq. m.",
                          "1 Bedroom",
                          "1 Room",
                          [],
                          "2500")


##muthi

room_muthimaya_forest_poolvilla = Room("Muthimaya",
                                       "1004",
                                        "MUTHI MAYA Forest Pool Villa",
                                       "164 sq. m.",
                                       "1 Bedroom",
                                       "1 Room",
                                       [],
                                       "2500")


##atta

room_one_bedroom_suite = Room("Atta",
                              "1005",
                              "One Bedroom Suite",
                              "65 sq. m.",
                              "1 Bedroom",
                              "1 Room",
                              [],
                              "2000")

room_one_bedroom_delight = Room("Atta",
                                "1006",
                                "One Bedroom Delight",
                                "65 sq. m.",
                                "1 Bedroom",
                                "1 Room",
                                [],
                                "2000")

room_two_bedroom_delight = Room("Atta",
                                "1007",
                                "Two Bedroom Delight",
                                "102 sq. m.",
                                "2 Bedroom",
                                "2 Room",
                                [],
                                "2500")

room_penthouse_suite = Room("Atta",
                            "1008",
                            "Penthouse Suite",
                            "235 sq. m.",
                            "2 Bedroom",
                            "2 Room",
                            [],
                            "2000")
mix = customer("mix",
               "saranji",
               "0627370763",
               "mixsaranji",
               "mix1234") 

xiw = admin("xiw",
            "tarijnaras",
            "0950988592",
            "xiwijnaras",
            "xiw1234")

sym = System()
testalog = RoomCatalog()
testalog.add_room(room_plantationview)
testalog.add_room(room_horizonview)
testalog.add_room(room_terrace_suite)
testalog.add_room(room_muthimaya_forest_poolvilla)
testalog.add_room(room_one_bedroom_suite)
testalog.add_room(room_one_bedroom_delight)
testalog.add_room(room_two_bedroom_delight)
testalog.add_room(room_penthouse_suite)
room_plantationview.add_interval(Interval("1-6-2018","9:00","10-6-2018","10:00"))
room_horizonview.add_interval(Interval("5-6-2018","9:00","10-6-2018","10:00"))
#function  หารถคันนั้น
sym.add_user(mix)
sym.add_user(xiw)

#function หาuser


#         "car": "ABZW-999",
#   "start_date": "11-6-2018",
#   "start_time": "9:00",
#   "end_date": "12-6-2018",
#   "end_time": "9:59"
# HOME
@app.get("/")
async def home():
    return {"Future_Car"}
#Login
@app.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    status_user= sym.check_user(form_data.username,form_data.password)
    if not status_user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = sym.get_user(form_data.username)
    return {"access_token": user._contact_username, "token_type": "bearer"}

#Register
@app.post("/users/registeration")
async def registeration(data:Registeration):
    if data.contact_type == "admin":
        sym.add_user(admin(data.contact_name,
                        data.contact_username, 
                        data.contact_phone_num, 
                        data.contact_password, 
                        data.contact_email))
        return {"message": "Register Success"}
    elif data.contact_type == "customer":
        sym.add_user(customer(data.contact_name,
                        data.contact_username, 
                        data.contact_phone_num, 
                        data.contact_password, 
                        data.contact_email))
        return {"message": "Register Success"}


@app.get("/users/me")
async def read_users_me(current_user = Depends(sym.get_current_user)):
    return current_user

#Cars
@app.get("/Rooms", tags=["Catalog"])
async def home():
    return {"catalog":[{"hotel_name": x.get_hotel_name(),
                        "room_number": x.get_car_model(),
                        "room_name": x.get_room_name(),
                        "room_area": x.get_room_area(),
                        "room_amount": x.get_room_amount()}
                       for x in testalog._room_lists]}

#Add_book
@app.post("/add_car", tags=["Cars"])
async def add_room_to_catalog(data:AddroomDTO):
    #ดักทะเบียน
    testalog.add_room(Room(
            data.hotel_name,
            data.room_number,
            data.room_name,
            data.room_area,
            data.number_of_bathroom,
            data.number_of_bedroom,
            data.room_amount,)
    )
    return {"status":"Add Success"}

@app.get("/search/search_car_by_brand", tags=["cars"])
async def search_car_by_brand(name:str):
    search_car = testalog.search_car_by_brand(name)
    return {"search found":[{"car_brand": x.get_car_brand(),
                        "car_model": x.get_car_model(),
                        "car_amount": x.get_car_amount(),
                        "car_plate_number": x.get_car_plate_number(),
                        "car_rating": x.get_rating_score()}
                       for x in search_car]}

@app.get("/search/search_car_by_model", tags=["cars"])
async def search_car_by_model(name:str):
    search_car = testalog.search_car_by_model(name)
    return {"search found":[{"car_brand": x.get_car_brand(),
                        "car_model": x.get_car_model(),
                        "car_amount": x.get_car_amount(),
                        "car_plate_number": x.get_car_plate_number(),
                        "car_rating": x.get_rating_score()}
                       for x in search_car]}

#Booking
@app.post("/get_available_car", tags=["Booking"])
async def get_available_car(data: AvalibleDTO):
    list_room = testalog.find_available_room(data.start_date,data.start_time,data.end_date,data.end_time)
    return list_room

@app.post("/book_car",tags = ["Booking"])
async def booking_car(data: BookingDTO,current_user = Depends(sym.get_current_user)):
    current_user._booking =testalog.book_room(data.car,data.start_date,data.start_time,data.end_date,data.end_time)
    return current_user._booking



##### CREDIT ###### E D I T I N G
@app.post("/add_credit_info", tags=["CreditCard"])
async def add_credit_info(data:CreditCard,current_user= Depends(sym.get_current_user)):
    current_user.add_credit_info(CreditInfo(data.exprie_card,data.card_number,data.security_credit))
    return current_user._credit_card

@app.post("/edit_credit_info", tags=["CreditCard"])
async def edit_credit_info(data:CreditCard,current_user= Depends(sym.get_current_user)):
    current_user._credit_card.edit_credit_info(data.exprie_card,data.card_number,data.security_credit)
    return current_user._credit_card



@app.get("/Payment",tags =["Payment"])
async def make_payment(current_user = Depends(sym.get_current_user)):
    status = False
    transaction_id = random.randint(100000000,999999999)
    rental_price = current_user._booking.get_price()
    credit_info = current_user._credit_card
    payment = Payment(rental_price,status,transaction_id,credit_info)
    return payment


# @app.post("/watch ",tags = ["Favourite"])
# async def add_favourite(data:FavouriteDTO):
#     petch.add_fav_car(data.car)
#     return {"status":"Success"}
    
    


#Credit_Card

#Payment


# @app.get("/watch_favourite_car",tags = ["Favourite"])
# async def add_favourite(request:Request):
#     data.username = FavouriteCar
#     petch.add_fav_car(data.car,data.username)
#     return "Add Favourite Successful"

# @app.get("/add_favorite",tags = ["booking"])
# async def

# booking =testalog.book_car("ABZW-999","11-6-2018","9:00","12-6-2018","9:59")
# booking.show_booking()