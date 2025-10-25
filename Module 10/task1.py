# Task 1

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


h = Elevator(1, 10)
h.go_to_floor(5)
h.go_to_floor(1)
