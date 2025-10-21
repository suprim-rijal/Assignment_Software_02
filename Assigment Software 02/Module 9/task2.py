#Task 2

class Car:
    def __init__(self,reg_num,max_speed):
        self.reg_num = reg_num
        self.max_speed = max_speed
        self.current_speed = 0
        self.travel_dis = 0

    def accelerate(self,speed_change):

        self.current_speed += speed_change

        if speed_change < 0:
             self.current_speed = 0
             
        elif self.current_speed > self.max_speed:
             self.current_speed = self.max_speed


car_1 = Car("ABC-123",142)
 
car_1.accelerate(30)
car_1.accelerate(70)
car_1.accelerate(50)

print(f"Current speed: {car_1.current_speed} km/h")

car_1.accelerate(-200)

print(f"Final Current speed: {car_1.current_speed} km/h")