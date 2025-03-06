class ElectricCar(Car):
    def __init__(self, color, capacity, engine_power, tyres, airbags, gear, speed, fuel, battery):
        super().__init__(color, capacity, engine_power, tyres, airbags, gear, speed, fuel)
        self.battery = battery  # Battery in kWh

    def charging(self):
        print(f"Charging the battery... Current battery level: {self.battery} kWh")

    def battery_level(self):
        print(f"Battery level: {self.battery} kWh")

# Example usage
tesla = ElectricCar("Blue", 5, "200 HP", 4, 6, "Automatic", 150, "Electric", 85)
tesla.start()
tesla.charging()
tesla.battery_level()
tesla.stop()
