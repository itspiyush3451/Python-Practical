# Task 1: Point Class
# This class represents a point in 3D space with x, y, z coordinates.
# It includes methods for arithmetic operations and comparisons.
class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    # Increment each coordinate by 1
    def increment(self):
        self.x += 1
        self.y += 1
        self.z += 1
    
    # Decrement each coordinate by 1
    def decrement(self):
        self.x -= 1
        self.y -= 1
        self.z -= 1
    
    # Add another point's coordinates to the current point
    def add(self, other):
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)
    
    # Less than comparison based on coordinates
    def __lt__(self, other):
        return (self.x, self.y, self.z) < (other.x, other.y, other.z)
    
    # Greater than comparison based on coordinates
    def __gt__(self, other):
        return (self.x, self.y, self.z) > (other.x, other.y, other.z)
    
    # Check if two points are equal
    def __eq__(self, other):
        return (self.x, self.y, self.z) == (other.x, other.y, other.z)
    
    # Determine which quadrant the point lies in (ignores z-axis for this calculation)
    def quadrant(self):
        if self.x > 0 and self.y > 0:
            return "First Quadrant"
        elif self.x < 0 and self.y > 0:
            return "Second Quadrant"
        elif self.x < 0 and self.y < 0:
            return "Third Quadrant"
        elif self.x > 0 and self.y < 0:
            return "Fourth Quadrant"
        else:
            return "On Axis"
    
    # String representation of a Point object
    def __str__(self):
        return f"Point({self.x}, {self.y}, {self.z})"

# Task 2: Watch Class
# Represents a watch with time and alarm functionality
class Watch:
    def __init__(self, hr, min, sec, alarm=None, type="Digital"):
        self.hr = hr
        self.min = min
        self.sec = sec
        self.alarm = alarm
        self.type = type
    
    # Set an alarm time
    def set_alarm(self, alarm_time):
        self.alarm = alarm_time
    
    # Stop the alarm
    def stop_alarm(self):
        self.alarm = None
    
    # Display the current time in HH:MM:SS format
    def show_time(self):
        return f"{self.hr:02}:{self.min:02}:{self.sec:02}"

# Task 3: Bank Account
# A simple bank account with deposit, withdraw, and balance check functionality
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    
    # Deposit money into the account
    def deposit_money(self, amount):
        self.balance += amount
    
    # Withdraw money if funds are sufficient
    def withdraw_money(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds!")
    
    # Display the account balance
    def show_balance(self):
        return f"Balance: {self.balance}"

# Task 4: Vehicle and Car Class
# Vehicle class represents general vehicle properties
class Vehicle:
    def __init__(self, color, capacity, engine_power, tyres):
        self.color = color
        self.capacity = capacity
        self.engine_power = engine_power
        self.tyres = tyres
    
    # Start the vehicle
    def start(self):
        print("Vehicle started.")
    
    # Stop the vehicle
    def stop(self):
        print("Vehicle stopped.")

# Car inherits from Vehicle and adds additional properties
class Car(Vehicle):
    def __init__(self, color, capacity, engine_power, tyres, airbags, gear, speed, fuel):
        super().__init__(color, capacity, engine_power, tyres)
        self.airbags = airbags
        self.gear = gear
        self.speed = speed
        self.fuel = fuel
    
    # Increase speed
    def accelerate(self):
        self.speed += 10
    
    # Refuel the car
    def fill_fuel(self, amount):
        self.fuel += amount
    
    # Play music in the car
    def play_music(self):
        print("Playing music.")
    
    # Turn on the AC
    def on_ac(self):
        print("AC turned on.")

# ElectricCar inherits from Car and adds battery-related functionality
class ElectricCar(Car):
    def __init__(self, color, capacity, engine_power, tyres, airbags, gear, speed, battery):
        super().__init__(color, capacity, engine_power, tyres, airbags, gear, speed, fuel=0)
        self.battery = battery
    
    # Start charging the electric car
    def charging(self):
        print("Car is charging.")
    
    # Check battery level
    def battery_level(self):
        return f"Battery level: {self.battery}%"

# Task 5: Person, Male, Female Classes
# Base class Person
class Person:
    def get_gender(self):
        pass

# Male class inherits from Person
class Male(Person):
    def get_gender(self):
        return "Male"

# Female class inherits from Person
class Female(Person):
    def get_gender(self):
        return "Female"

# Task 6: OOP Concepts in Pharmaceuticals
# Abstract class for different types of medicine
from abc import ABC, abstractmethod

class Medicine(ABC):
    @abstractmethod
    def use(self):
        pass

# Tablet class implements Medicine
class Tablet(Medicine):
    def use(self):
        return "Swallow with water."

# Syrup class implements Medicine
class Syrup(Medicine):
    def use(self):
        return "Take with a spoon."

# Capsule class implements Medicine
class Capsule(Medicine):
    def use(self):
        return "Take with warm water."

# Doctor class prescribes medicines
class Doctor:
    def prescribe(self, medicine: Medicine):
        return medicine.use()

# Testing example
# Creating a doctor and a tablet instance to test polymorphism
doc = Doctor()
tab = Tablet()
print(doc.prescribe(tab))