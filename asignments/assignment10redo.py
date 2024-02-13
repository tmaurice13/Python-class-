class Car:
    def __init__(self,name,make,year):
        self.name=name
        self.make=make
        self.year=year
        print(f'Car_name: {self.name}, car_make: {self.make}, Year: {self.year}')
car_1=Car("mazda", 2021 ,2021)