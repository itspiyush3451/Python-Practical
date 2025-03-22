# 🐍 Python Practicals

![Python Logo](https://www.python.org/static/community_logos/python-logo-generic.svg)

> A comprehensive collection of Python programming exercises and examples for college students. This repository serves as a practical learning resource to complement your Python course curriculum.

[![GitHub stars](https://img.shields.io/github/stars/itspiyush3451/Python-Practical?style=social)](https://github.com/itspiyush3451/Python-Practical/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/itspiyush3451/Python-Practical?style=social)](https://github.com/itspiyush3451/Python-Practical/network/members)
[![GitHub issues](https://img.shields.io/github/issues/itspiyush3451/Python-Practical)](https://github.com/itspiyush3451/Python-Practical/issues)
[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/downloads/)

## 📚 Repository Structure

This repository is organized into modules, each focusing on specific Python concepts:

| Module | Topics Covered | Key Concepts |
|--------|---------------|-------------|
| [Module01](./Module01/) | Basic Programs | Variables, Data Types, Input/Output |
| [Module02](./Module02/) | Basic Programs | Operators, Expressions, Basic Math |
| [Module03](./Module03/) | Dictionaries & Sets | Hash Tables, Key-Value Pairs, Set Operations |
| [Module04](./Module04/) | Mathematical Algorithms & Data Structures | GCD, Fibonacci, Sum of Digits, Lists, Tuples |
| [Module05](./Module05/) | Loops & Conditionals | Even/Odd Detection, Leap Year Calculation, Control Flow |
| [Module06](./Module06/) | String Handling | Palindromes, Word Count, String Manipulation |
| [Module07](./Module07/) | Functions & Recursion | Function Definition, Parameter Passing, Basic Recursion |
| [Module08](./Module08/) | Advanced Functions & Recursion | Recursive Problem Solving, Advanced Function Concepts |
| [Module09](./Module09/) | Special Function Parameters & List Operations | `*args`, Duplicate Removal, Stack Implementation |
| [Module10](./Module10/) | Packages & Modules | Module Creation, Package Structure, Imports |
| [Module11](./Module11/) | Object-Oriented Programming | Classes, Inheritance, Encapsulation |
| [Module12](./Module12/) | Regular Expressions | Pattern Matching, Text Processing |

## 🚀 Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- [Python 3.x](https://www.python.org/downloads/) - The programming language used
- A text editor or IDE:
  - [Visual Studio Code](https://code.visualstudio.com/) (recommended)
  - [PyCharm](https://www.jetbrains.com/pycharm/)
  - [Jupyter Notebook](https://jupyter.org/) (for interactive learning)
- Basic understanding of programming concepts

### Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/itspiyush3451/Python-Practical.git
   ```

2. **Navigate to the repository**:
   ```bash
   cd Python-Practical
   ```

3. **Explore a specific module**:
   ```bash
   cd Module01
   ```

4. **Run a Python file**:
   ```bash
   python example_program.py
   ```

### Quick Start Guide

For those who want to jump right in:

1. **Choose a topic** you're interested in learning from the module list
2. **Navigate to that module** folder
3. **Read the README.md** file in that module (if available) for specific instructions
4. **Open and study** the example programs
5. **Modify and experiment** with the code to deepen your understanding

## 📝 Learning Path

Suggested order for beginners:

1. **Start with Module01 and Module02** to understand Python basics
2. **Move to Module05** to learn about control structures
3. **Continue to Module04** to understand data structures
4. **Explore Module06** for string manipulation techniques
5. **Learn functions with Module07 and Module08**
6. **Dive into OOP with Module11**
7. **Finish with advanced topics** in the remaining modules

## 🤝 Contributing

We welcome contributions from all classmates! Help make this repository a comprehensive resource for learning Python.

### Ways to Contribute

- **Add New Examples**: Create additional examples that demonstrate concepts
- **Improve Existing Code**: Optimize or refactor code for better readability
- **Fix Bugs**: Help identify and fix issues
- **Add Comments**: Enhance code documentation with clear explanations
- **Create Tutorials**: Write step-by-step guides for complex topics
- **Add Practical Challenges**: Develop practice exercises with solutions

### Contribution Process

1. **Fork the Repository**:
   <br>Click the "Fork" button at the top right of this repository

2. **Clone Your Fork**:
   ```bash
   git clone https://github.com/YOUR-USERNAME/Python-Practical.git
   cd Python-Practical
   ```

3. **Create a Branch**:
   ```bash
   git checkout -b contribution/your-feature-name
   ```

4. **Make Your Changes**:
   <br>Add or modify files as needed

5. **Test Your Changes**:
   <br>Ensure all code runs correctly before submitting

6. **Commit Your Changes**:
   ```bash
   git add .
   git commit -m "Add feature: brief description of changes"
   ```

7. **Push to Your Fork**:
   ```bash
   git push origin contribution/your-feature-name
   ```

8. **Create a Pull Request**:
   <br>Go to the original repository and click "New Pull Request"

## 📊 Module Highlights

<details>
<summary><b>Module01-02: Python Basics</b></summary>
<br>
Learn the fundamental building blocks of Python programming including variables, data types, operators, and basic syntax.

```python
# Example: Hello World program
print("Hello, Python World!")

# Example: Basic arithmetic
a = 10
b = 5
print(f"Sum: {a + b}")
print(f"Difference: {a - b}")
print(f"Product: {a * b}")
print(f"Quotient: {a / b}")
```
</details>

<details>
<summary><b>Module05: Control Flow</b></summary>
<br>
Master conditional statements and loops to control program execution.

```python
# Example: Check if a number is even or odd
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

# Example: Print first 10 Fibonacci numbers
a, b = 0, 1
for i in range(10):
    print(a, end=" ")
    a, b = b, a + b
```
</details>

<details>
<summary><b>Module11: Object-Oriented Programming</b></summary>
<br>
Understand how to create classes, objects, and implement inheritance.

```python
# Example: A simple class
class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        
    def display_info(self):
        print(f"Student: {self.name}, Roll Number: {self.roll_number}")

# Creating an object
student1 = Student("Alex", "CS101")
student1.display_info()
```
</details>

## 📚 Additional Resources

- **Books**:
  - "Python Crash Course" by Eric Matthes
  - "Automate the Boring Stuff with Python" by Al Sweigart

- **Online Courses**:
  - [Coursera - Python for Everybody](https://www.coursera.org/specializations/python)
  - [edX - Introduction to Computer Science and Programming Using Python](https://www.edx.org/course/introduction-to-computer-science-and-programming-7)

- **Websites**:
  - [Python Official Documentation](https://docs.python.org/3/)
  - [Real Python](https://realpython.com/)
  - [PyBites](https://pybit.es/articles/)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ✨ Acknowledgements

- Thanks to all contributors who have helped build this resource
- Special thanks to our Python programming course instructors
- Python community for creating such an amazing programming language

---

<div align="center">
  Made with ❤️ by Python enthusiasts for Python learners
  
  <a href="https://github.com/itspiyush3451">@itspiyush3451</a> and contributors
  
  <p>⭐ Star this repository if you find it helpful! ⭐</p>
</div>
