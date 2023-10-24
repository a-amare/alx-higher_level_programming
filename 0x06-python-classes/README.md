# Square Class

This project is designed to help you understand and practice Object-Oriented Programming (OOP) in Python, specifically focusing on the concept of classes and objects. You'll implement a `Square` class with various features, gradually building upon your knowledge. Here's what you need to know and implement:

## Learning Objectives

After completing this project, you should be able to explain the following OOP concepts:

- Why Python programming is awesome
- What is OOP (Object-Oriented Programming)
- "First-class everything"
- What is a class
- What is an object and an instance
- The difference between a class and an object or instance
- What is an attribute
- How to use public, protected, and private attributes
- What is `self`
- What is a method
- The special `__init__` method and how to use it
- Data Abstraction, Data Encapsulation, and Information Hiding
- What is a property
- The difference between an attribute and a property in Python
- The Pythonic way to write getters and setters in Python
- How to dynamically create arbitrary new attributes for existing instances of a class
- How to bind attributes to objects and classes
- What is the `__dict__` of a class and/or instance of a class and what does it contain
- How Python finds the attributes of an object or class
- How to use the `getattr` function

## Project Structure

This project consists of several tasks, each building upon the previous one. You'll create a `Square` class with various features. Here's an overview of the tasks:

### Task 0: My First Square

Create an empty `Square` class.

### Task 1: Square with Size

Enhance the `Square` class to include a private instance attribute called `size`. The class should allow instantiation with a specified size and prevent direct access to this attribute.

### Task 2: Size Validation

Continue improving the `Square` class by adding validation for the `size` attribute. The size must be an integer, and if it's less than 0, an exception should be raised.

### Task 3: Area of a Square

Enhance the `Square` class with a public instance method called `area` that returns the area of the square.

### Task 4: Access and Update Private Attribute

Implement getter and setter methods for the private `size` attribute in the `Square` class. These methods will ensure that the size attribute is an integer and handle any type or value validation.

### Task 5: Printing a Square

Add a public instance method named `my_print` to the `Square` class. This method will print the square using `#` characters. If the size is 0, it will print an empty line.

### Task 6: Coordinates of a Square

Extend the `Square` class with a private instance attribute called `position`. Implement getter and setter methods for this attribute, ensuring it's a tuple of two positive integers. The `my_print` method should now consider the position attribute to determine the square's alignment in the output.

## Requirements

- Use only the allowed editors: vi, vim, emacs.
- All code will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.8.5.
- All Python files should end with a new line.
- The first line of all Python files should be `#!/usr/bin/python3`.
- A `README.md` file at the root of the project is mandatory.
- Code should follow the `pycodestyle` (PEP 8) style guide.
- All Python files must be executable.
- Provide documentation for modules, classes, and functions using docstrings.

## Project Structure

- `0-square.py`: Task 0 implementation.
- `1-square.py`: Task 1 implementation.
- `2-square.py`: Task 2 implementation.
- `3-square.py`: Task 3 implementation.
- `4-square.py`: Task 4 implementation.
- `5-square.py`: Task 5 implementation.
- `6-square.py`: Task 6 implementation.

## Running the Project

You can run the project by executing the provided main files for each task. For example:

```bash
$ ./0-main.py
$ ./1-main.py
$ ./2-main.py
$ ./3-main.py
$ ./4-main.py
$ ./5-main.py
$ ./6-main.py
```

These main files test the functionality of the `Square` class for each task.
