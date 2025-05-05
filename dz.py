
class Human:
    default_name = "name"
    default_age = 0

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = 0

    def info(self):
        print(f"Имя: {self.name} \n"
              f"Возраст: {self.age} \n"
              f"Деньги: {self.__money} \n"
              f"Дом: {self.__house} ")

    @staticmethod
    def default_info():
        print(f"{Human.default_name} \n"
              f"{Human.default_age}")

    def __make_deal(self, house, price):
        self.__house = house
        self.__money -= price
        print("Вы купили дом")

    def earn_money(self, money):
        self.__money += money

    def buy_house(self, house):
        if self.__money > house._price:
            self.__make_deal(house, house._price)
        else:
            print("Недостаточно денег")

class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        return self._price - (self._price * discount // 100)


class SmallHouse(House):
    def __init__(self):
        self._area = 40



user1 = Human("userName", 13)
user1.earn_money(1000)
user1.info()
house1 = House(120, 15000)
print(house1.__dict__)
user1.buy_house(house1)
user1.info()






