"""
- Everything is an object in Python
- Object/Class, Attribute(variables that belong to the class), Methods(functions defined inside the class)

-> age_string = str(25) -> instance
-> age_string.center(85) -> the instance is responsible, not the class that is instatieted from


- Design (write simple and clean code):
 -> break code into multiple files/modules
 -> put functions into a class
 
- DRY - Don't repeat yourself 
-> Inheritance(Give to a child the attributes and methods of the parent)

- Super function -> reuse code written in a super class

- not limited to a single parent class

- magic methods:
__str__ - Control how your instances turn into strings
__int__ - Control int() conversion
__init__ - Customize the initialization of your instances

- Subclassing built-ins
-> customizing mutable data: __init__
-> customizing immutable data: __new__

- Special methods
"""