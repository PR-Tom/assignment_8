class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current_floor = bottom

    def floor_up(self):
        if self.current_floor < self.top:
            self.current_floor += 1
            print(f"Elevator is now on floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom:
            self.current_floor -= 1
            print(f"Elevator is now on floor {self.current_floor}")

    def go_to_floor(self, target_floor):
        if target_floor < self.bottom or target_floor > self.top:
            print("Invalid floor")
            return

        while self.current_floor < target_floor:
            self.floor_up()

        while self.current_floor > target_floor:
            self.floor_down()


class Building:
    def __init__(self, bottom, top, elevator_count):
        self.elevators = []

        for _ in range(elevator_count):
            self.elevators.append(Elevator(bottom, top))

    def run_elevator(self, elevator_number, destination_floor):
        if elevator_number < 0 or elevator_number >= len(self.elevators):
            print("Invalid elevator number")
            return

        print(f"\nRunning elevator {elevator_number}")
        self.elevators[elevator_number].go_to_floor(destination_floor)


building = Building(1, 10, 3)

building.run_elevator(0, 5)
building.run_elevator(1, 8)
building.run_elevator(2, 3)


building.run_elevator(0, 1)
