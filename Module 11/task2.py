 
#Task 2
import random
class Car:
    def __init__(self,reg_num,max_speed):
        self.reg_num = reg_num
        self.max_speed = max_speed
        self.current_speed = 0
        self.travel_dis = 0

    def accelerate(self,speed_change):

        self.current_speed += speed_change
        if self.current_speed < 0:
             self.current_speed = 0

        elif self.current_speed > self.max_speed:
             self.current_speed = self.max_speed

    def drive(self,hours):
        self.travel_dis += self.current_speed * hours
        

class ElectricCar(Car):
    def __init__(self,reg_num,max_speed,battery_capacity):
        super().__init__(reg_num,max_speed)
        self.battery_capacity = battery_capacity
        


class GasolineCar(Car):
    def __init__(self,reg_num,max_speed,volume_capacity):
        super().__init__(reg_num,max_speed)
        self.volume_capacity = volume_capacity


object1 = ElectricCar("ABC-15",180,52.5)
object2 = GasolineCar("ACD-123",165,32.3)

object1.accelerate(150)
object2.accelerate(200)

object1.drive(3)
object2.drive(3)

print(f"Counter of Electric Car is: {object1.travel_dis} km")
print(f"Counter of Gasoline Car is: {object2.travel_dis} km")

























