# Task 3

class Elevator:

    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.at_floor = bottom

    def go_to_floor(self, goingto_floor):
        if goingto_floor > self.top or goingto_floor < self.bottom:
            print("That floor doesn't exist in this building.")
            return
        
        print(f"Starting at floor {self.at_floor}")
        while self.at_floor < goingto_floor:
            self.floor_up()

        while self.at_floor > goingto_floor:
            self.floor_down()

        print(f"Arrived at floor {self.at_floor}")

# Task 2

class Elevator:

    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.at_floor = bottom

    def go_to_floor(self, goingto_floor):
        if goingto_floor > self.top or goingto_floor < self.bottom:
            print("That floor doesn't exist in this building.")
            return
        
        print(f"Starting at floor {self.at_floor}")
        while self.at_floor < goingto_floor:
            self.floor_up()

        while self.at_floor > goingto_floor:
            self.floor_down()

        print(f"Arrived at floor {self.at_floor}")

    def floor_up(self):
        if self.at_floor >= self.top:
            print("Already at the top floor!")
        else:
            self.at_floor += 1
            print(f"Elevator moved up! Now at floor {self.at_floor}")

    def floor_down(self):
        if self.at_floor <= self.bottom:
            print("Already at the bottom floor!")
        else:
            self.at_floor -= 1
            print(f"Elevator moved down! Now at floor {self.at_floor}")

class Building:

    def __init__(self, bottom, top,num_elevators):
        self.bottom = bottom
        self.top = top
        self.num_elevators = num_elevators
        self.elevators = []
        for i in range(num_elevators):
            self.elevators.append(Elevator(bottom, top))

    def run_elevator(self,elevators_num,goingto_floor):
        if elevators_num < 1 or elevators_num > self.num_elevators:
            print("That elevator number doesn't exist in this building.")
            return
        print(f"\nRunning elevator {elevators_num} to floor {goingto_floor}:")
        elevator = self.elevators[elevators_num - 1]
        elevator.go_to_floor(goingto_floor)

    def fire_alarm(self):
        
        print("FIRE ALARM!!!................................................................")
        for i in range(len(self.elevators)):
           print(f"\nMoving elevator {i + 1} to bottom:")
           self.elevators[i].go_to_floor(self.bottom)



building = Building(1, 10, 2)
building.run_elevator(1, 5)
building.run_elevator(3, 1)

building.fire_alarm()

