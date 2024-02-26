# ### 7 Question
# Write a Python program to create a decorator that prints the arguments and return value of a function. / Напишите программу на Python, чтобы создать декоратор, печатающая аргументы и возвращаемое значение функции.

def say_hello(func):
    
    def ihnner(a):
        print("Say hello")
        func(a)
        print("Salom jahon")
    
    return ihnner



@say_hello
def hi_man(a):
    print(a)

a = input()

hi_man(a)