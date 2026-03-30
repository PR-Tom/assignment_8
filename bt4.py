import random


class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        self.current_speed += speed_change
        if self.current_speed < 0:
            self.current_speed = 0
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)

    def print_status(self):
        print(f"\n{'Reg.No':<10} {'Max Speed':<10} {'Speed':<10} {'Distance':<10}")
        print("-" * 45)
        for car in self.cars:
            print(f"{car.registration_number:<10} "
                  f"{car.max_speed:<10} "
                  f"{car.current_speed:<10} "
                  f"{car.travelled_distance:<10.1f}")

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                return True
        return False


cars = []
for i in range(1, 11):
    cars.append(Car(f"ABC-{i}", random.randint(150, 200)))

race = Race("Grand Demolition Derby", 8000, cars)

hours = 0

while not race.race_finished():
    race.hour_passes()
    hours += 1

    if hours % 10 == 0:
        print(f"\n--- Hour {hours} ---")
        race.print_status()

print("\n🏁 RACE FINISHED 🏁")
print(f"Total hours: {hours}")
race.print_status()
