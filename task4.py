# ### 4 Question
# Write a Python program to create a calculator class. Include methods for basic arithmetic operations. / Напишите программу на Python для создания класса калькулятора. Включите методы для основных арифметических операций.

class Calculate:

    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def addition(self):
        return self.a + self.b
    
    def minus(self):
        return self.a - self.b
    
    def multiply(self):
        return self.a * self.b
    
    def define(self):
        return self.a // self.b
    
    def modd(self):
        return self.a % self.b
    
a = int(input())
char = input()
b = int(input())
calc = Calculate(a, b)

match char:
    case "+":
        print(calc.addition())
    
    case "-":
        print(calc.minus())

    case "*":
        print(calc.multiply())

    case "/":
        print(calc.define())

    case "%":
        print(calc.modd())       