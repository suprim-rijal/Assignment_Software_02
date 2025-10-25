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
        
class Race:
    def __init__(self,name,distance,car_lists):
        self.name = name
        self.distance = distance
        self.car_lists = car_lists

    def hour_passes(self):
        for car in self.car_lists:
            change = random.randint(-10, 15)
            car.accelerate(change)
            car.drive(1)
           

    def print_status(self, hours):
        print(f"\nHour Passed:{hours}\n")
        print(f"{'Car':<10}{'Max Speed':<12}{'Current Speed':<16}{'Distance (km)':<15}")

        for car in self.car_lists:
            print(f"{car.reg_num:<10}{car.max_speed:<12}{car.current_speed:<16}{car.travel_dis:<15.2f}")

    def race_finished(self):
        for car in self.car_lists:
            if car.travel_dis >= self.distance:
                return True
        return False


car_list = []
hour_passed = 0
for i in range(1, 11):
    reg_num = f"ABC-{i}"
    max_speed = random.randint(100, 200)
    car = Car(reg_num, max_speed)
    car_list.append(car)

race = Race("Grand Demolition Derby", 8000, car_list)

while not race.race_finished():
    hour_passed += 1
    race.hour_passes()

    if hour_passed % 10 == 0: 
        race.print_status(hour_passed)

race.print_status(hour_passed)
print("The race has finished!!!!")




