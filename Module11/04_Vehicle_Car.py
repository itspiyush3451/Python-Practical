class Vehicle:
    def __init__(self, color, capacity, engine_power, tyres):
        self.color = color
        self.capacity = capacity
        self.engine_power = engine_power
        self.tyres = tyres

    def start(self):
        print("Vehicle started")

    def stop(self):
        print("Vehicle stopped")

class Car(Vehicle):
    def __init__(self, color, capacity, engine_power, tyres, airbags, gear, speed, fuel):
        super().__init__(color, capacity, engine_power, tyres)
        self.airbags = airbags
        self.gear = gear
        self.speed = speed
        self.fuel = fuel

    def accelerate(self):
        print("Car is accelerating")

    def fill_fuel(self):
        print("Fuel tank is being refilled")

    def play_music(self):
        print("Playing music")

    def on_AC(self):
        print("Air Conditioner turned on")

# Example usage
car = Car("Red", 5, "150 HP", 4, 2, "Automatic", 120, "Petrol")
car.start()
car.accelerate()
car.play_music()
car.stop()
