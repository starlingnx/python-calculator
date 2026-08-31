"""
Calculator Logic Module
Handles all mathematical operations for the calculator application.
"""

import math


class Calculator:
    """A comprehensive calculator supporting basic and advanced operations."""
    
    def __init__(self):
        self.result = 0
        self.history = []
    
    def add(self, a, b):
        """Addition operation."""
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a, b):
        """Subtraction operation."""
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a, b):
        """Multiplication operation."""
        result = a * b
        self.history.append(f"{a} × {b} = {result}")
        return result
    
    def divide(self, a, b):
        """Division operation with zero division check."""
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        result = a / b
        self.history.append(f"{a} ÷ {b} = {result}")
        return result
    
    def power(self, a, b):
        """Power operation (a^b)."""
        result = a ** b
        self.history.append(f"{a}^{b} = {result}")
        return result
    
    def square_root(self, a):
        """Square root operation."""
        if a < 0:
            raise ValueError("Cannot calculate square root of negative number!")
        result = math.sqrt(a)
        self.history.append(f"√{a} = {result}")
        return result
    
    def percentage(self, a, b):
        """Percentage calculation (a% of b)."""
        result = (a / 100) * b
        self.history.append(f"{a}% of {b} = {result}")
        return result
    
    def sine(self, angle):
        """Sine operation (angle in degrees)."""
        result = math.sin(math.radians(angle))
        self.history.append(f"sin({angle}°) = {result}")
        return result
    
    def cosine(self, angle):
        """Cosine operation (angle in degrees)."""
        result = math.cos(math.radians(angle))
        self.history.append(f"cos({angle}°) = {result}")
        return result
    
    def tangent(self, angle):
        """Tangent operation (angle in degrees)."""
        result = math.tan(math.radians(angle))
        self.history.append(f"tan({angle}°) = {result}")
        return result
    
    def logarithm(self, a, base=10):
        """Logarithm operation."""
        if a <= 0:
            raise ValueError("Logarithm undefined for non-positive numbers!")
        result = math.log(a, base)
        self.history.append(f"log{base}({a}) = {result}")
        return result
    
    def factorial(self, n):
        """Factorial operation."""
        if n < 0:
            raise ValueError("Factorial undefined for negative numbers!")
        result = math.factorial(int(n))
        self.history.append(f"{n}! = {result}")
        return result
    
    def get_history(self):
        """Get all calculation history."""
        return self.history
    
    def clear_history(self):
        """Clear calculation history."""
        self.history = []
    
    def evaluate(self, expression):
        """Safely evaluate mathematical expression."""
        try:
            result = eval(expression)
            self.history.append(f"{expression} = {result}")
            return result
        except Exception as e:
            raise ValueError(f"Invalid expression: {str(e)}")
