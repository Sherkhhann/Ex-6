# ### 6 Question
# Write a Python program to create a class representing a shopping cart. Include methods for adding and removing items, and calculating the total price. / Напишите программу на Python, чтобы создать класс, представляющий корзину покупок. Включите методы добавления и удаления элементов, а также расчета общей цены.

class ShopCart:
    
    def __init__(self):
        self.list_shop = []

    def add_new(self, title, price, ):
        dict_name = {title: price}
        self.list_shop.append(dict_name)

    def get_info(self):
        if not self.list_shop:
            print("Your list is empty")
        else:
            for item in self.list_shop:
                for key,value in item.items():
                    print(f"{key}: {value}$")

    def del_new(self, title_new):
        for item in self.list_shop:
            if title_new in item.items():
                self.list_shop.remove(item)
        else:
            print(f"{title_new} not found!")
    
    def count_all(self, sum = 0):
        for d in self.list_shop:
            for j in d.values():
                sum += j
        print(f"Your total: {sum}$")

    
bag = ShopCart()
while True:
    print("""
a - add,
d - delete,
g - get info,
c - count,
e - exit""")
    
    choise = input("Which? ").lower()

    match choise:

        case "a":
            bag.add_new(input("Name: "), int(input("Price: ")))

        case "d":
            bag.del_new(input("Name: "))

        case "g":
            bag.get_info()

        case "c":
            bag.count_all()

        case "e":
            break
        case _:
                print("Invalid choice. Please enter a valid option.")