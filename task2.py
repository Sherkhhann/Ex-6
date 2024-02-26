# ### 2 Question
# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
# Напишите программу, которая принимает из консоли последовательность чисел, разделенных запятыми, и генерирует список и кортеж, содержащий каждое число.
# Input:
# 34,67,55,33,12,98
# Output: 
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

a = input().split(",")

print(a)
print(tuple(a))