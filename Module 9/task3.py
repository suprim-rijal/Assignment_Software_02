#Task 3

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

    def drive(self,hours):

        self.hours = hours

        self.travel_dis += self.current_speed* self.hours
        




car_1 = Car("ABC-123",142)
 
car_1.accelerate(60)
car_1.drive(1.5)

print(f"Travelled Distance: {car_1.travel_dis} km/h")

