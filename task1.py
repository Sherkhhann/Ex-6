# ### 1 Question
# Random Lottery Pick. Generate 100 random lottery tickets and pick two lucky tickets from it as a winner.
# Случайный лотерейный выбор. Создайте 100 случайных лотерейных билетов и выберите из них два счастливых билета в качестве победителя.
#     Note you must adhere to the following conditions(что необходимо соблюдать следующие условия:):
#     The lottery number must be 10 digits long(Номер лотереи должен состоять из 10 цифр).
#     All 100 ticket number must be unique(Все 100 номеров билетов должны быть уникальными).

import random

def loterry():
    lucky = []
    for i in range(2):
        s = random.randint(1000000000, 9999999999)
        if s not in lucky:
            lucky.append(s)
    
    return lucky

print(loterry())
