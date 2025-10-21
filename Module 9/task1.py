#Task 1

class Car:
    def __init__(self,reg_num,max_speed):
        self.reg_num = reg_num
        self.max_speed = max_speed
        self.current_speed = 0
        self.travel_dis = 0

car_1 = Car("ABC-123",142)
print(f"Registration number: {car_1.reg_num}")
print(f"Maximum speed: {car_1.max_speed} km/h")
print(f"Current speed: {car_1.current_speed} km/h")
print(f"Travelled distance: {car_1.travel_dis} km")