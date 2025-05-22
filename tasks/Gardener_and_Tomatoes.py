import random

class Tomato:
    states = {
        1 : "Отсутствует",
        2 : "Цветение",
        3 : "Зеленый",
        4 : "Красный"
    }

    def __init__(self, index):
        self.__index = index
        # self.__state = self.states[1]
        self.__state = 1

    def grow(self):
        self.__state += 1
        # match self.__state:
        #     case "Отсутствует":
        #         self.__state = self.states[2]
        #     case "Цветение":
        #         self.__state = self.states[3]
        #     case "Зеленый":
        #         self.__state = self.states[4]

    def is_ripe(self):
        return self.__state == "Красный"

# class TomatoBush:
#     tomatoes = []
#     def __init__(self):
#         self.tomatoes = Tomato(12322)


s = Tomato(182768)
print(s.__dict__)
s.grow()
print(s.__dict__)
s.grow()
print(s.__dict__)
print(s.is_ripe())
s.grow()
print(s.__dict__)
print(s.is_ripe())

