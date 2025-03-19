# Task 6: OOP Concepts in Pharmaceuticals
# Using Inheritance, Encapsulation, Abstraction, and Polymorphism

from abc import ABC, abstractmethod

# Abstract class for drug formulations demonstrating Abstraction
class DrugFormulation(ABC):
    def __init__(self, name, dosage, manufacturer):
        self._name = name  # Encapsulation: Protecting sensitive drug data
        self._dosage = dosage
        self._manufacturer = manufacturer

    @abstractmethod
    def administer(self):
        pass

    def get_info(self):
        return f"{self._name} ({self._dosage}) by {self._manufacturer}"

# Tablet class inherits from DrugFormulation
class Tablet(DrugFormulation):
    def administer(self):
        return f"Administer {self._name} tablet orally with water."

# Capsule class inherits from DrugFormulation
class Capsule(DrugFormulation):
    def administer(self):
        return f"Administer {self._name} capsule with warm water."

# Injection class inherits from DrugFormulation
class Injection(DrugFormulation):
    def administer(self):
        return f"Administer {self._name} injection intravenously."

# Doctor class prescribing different drug formulations
def prescribe_drug(drug: DrugFormulation):
    return drug.administer()

# Testing polymorphism with different drug types
tablet = Tablet("Paracetamol", "500mg", "PharmaCorp")
capsule = Capsule("Amoxicillin", "250mg", "MediHealth")
injection = Injection("Insulin", "10ml", "BioCare")

print(prescribe_drug(tablet))
print(prescribe_drug(capsule))
print(prescribe_drug(injection))

# Additional Programs

# Program to find the sum of an array
def sum_of_array(arr):
    return sum(arr)

# Program to find the largest element in an array
def largest_element(arr):
    return max(arr)

# Program to split the array and add the first part to the end
def split_and_add(arr, split_index):
    return arr[split_index:] + arr[:split_index]

# Program to add two matrices
def add_matrices(matrix1, matrix2):
    return [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

# Example usage
arr = [1, 2, 3, 4, 5]
print("Sum of array:", sum_of_array(arr))
print("Largest element in array:", largest_element(arr))
print("Array after splitting and adding:", split_and_add(arr, 2))

matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
print("Sum of matrices:", add_matrices(matrix1, matrix2))
