# ### 5 Question
# Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age. Use incapsulation methods as well. / Напишите программу на Python для создания класса человека. Включите такие атрибуты, как имя, страна и дата рождения. Реализуйте метод определения возраста человека. Также используйте методы инкапсуляции.

# from datetime import datetime

# class Person:

#     def __init__(self, name, country, date_birth):
#         self.__name = name
#         self.__country = country
#         self.__date_birth = datetime.strptime(date_birth, "%Y-%m-%d")
#         self.current_time = datetime.now()
#     def get_info(self):
#         yo = self.__date_birth - self.current_time
#         return f"My name is {self.__name}. I'm from {self.__country}. I'm {yo.days // 365} years old"

# your_name = input()
# your_country = input()
# day_birth = datetime.datetime.strptime(input("Enter dd/mm/yy - > "), "%d/%m/%Y")

# pers = Person(your_name, your_country, day_birth)

# print(pers.get_info())

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     # def geti(self):
#     #     return self.x

#     def __repr__(self):
#         return f"Point({self.x}, {self.y})"
    

# per = Point("5", "6")
# print(per)

import random

s = random.uniform(0, 10)

print(s)