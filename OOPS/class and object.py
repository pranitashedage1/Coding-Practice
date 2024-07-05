'''
Class - It is an user-defined prototype for the object which has set of attributes that characterize the 
any object of the class.
attributes - class variables, instance varibales, methods

Object - It is an instance of certain class.

'''
class Car:
    def __init__(self, car_type, car_name) -> None:
        self.car_type = car_type
        self.car_name = car_name

    def carInfo(self):
        print(f"Car_type = {self.car_type} and car_name = {self.car_name}")


tata = Car(car_type='Tata', car_name='SUV')
tata.carInfo()

