
from User import Owner
from Class_new.CarCatalog import CarCatalog
from Class_new.Car import Car
future = Owner("futurenaja",
               "futureza567",
               "0930036622",
               "123456789",
               "65010671@gmail.com")
cara =Car("BMW",
          "I8",
          "Engine",
          "200km",
          "200CC",
          "2Door",
          "3year",
          "2seat",
          100,
          "car_about",
          "ABZW-908")

carb =Car("Ferrari",
          "F1",
          "Engine",
          "200km",
          "300CC",
          "4Door",
          "3year",
          "2seat",
          200,
          "car_about",
          "ABZW-999")

carc =Car("Porsche",
          "M8",
          "Engine",
          "200km",
          "300CC",
          "4Door",
          "3year",
          "2seat",
          300,
          "car_about",
          "ABZW-999")


testalog = CarCatalog()
future.add_car(cara,testalog)
future.add_car(carb,testalog)
future.add_car(carc,testalog)
testalog.get_all_car_detail()