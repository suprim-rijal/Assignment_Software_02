#Task 4
import random
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
        

car_lists =[]
race = True
hourspassed = 0


for i in range(1,11):
    reg_num = f"ABC-{i}"
    max_speed = random.randint(100,200)
    car = Car(reg_num,max_speed)
    car_lists.append(car)

while race:
    hourspassed+=1
    for car in car_lists:
        change=random.randint(-10,15)
        car.accelerate(change)
        car.drive(1)
    if car.travel_dis >= 10000:
        race = False
        break

print(f"\nHour Passed:{hourspassed}\n")
print(f"{'Car':<10}{'Max Speed':<12}{'Current Speed':<16}{'Distance (km)':<15}")


for car in car_lists:
    print(f"{car.reg_num:<10}{car.max_speed:<12}{car.current_speed:<16}{car.travel_dis:<15.2f}")