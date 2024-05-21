#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

def greet(name="Guido"):
    print(f"Hello, {name}!")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

def add(num1, num2):
    return num1 + num2 

def halve(number):
    return number / 2  

greet_programmer()          
greet()                    
greet("Alice")              
greet_with_default()       
greet_with_default("Bob")  
print(add(3, 5))  
print(halve(10))  