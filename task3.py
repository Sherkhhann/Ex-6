# ### 3 Question
# Create a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.
# Создайте генератором, который может перебирать числа, кратные 7, в заданном диапазоне от 0 до n.
# Input:
# n = 30
# Output:
# 7 14 21 28

def gen_seven(n):
    for i in range(1, n):
        if i%7 == 0:
            yield i

s = gen_seven(30)

for j in s:
    print(j, end=" ")
