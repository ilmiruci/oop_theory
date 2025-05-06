class Human:
    default_name: str = "Unknown"
    default_age: int = 0

    def __init__(self, name: str = default_name, age: int = default_age) -> None:
        self.name: str = name
        self.age: int = age
        self.__money: int = 0
        self.__house = None

    def info(self) -> None:
        print(f"Имя: {self.name}\n"
              f"Возраст: {self.age}\n"
              f"Деньги: {self.__money}\n"
              f"Дом: {self.__house} ")

    @staticmethod
    def default_info() -> None:
        print(f"{Human.default_name}\n"
              f"{Human.default_age}")

    def __make_deal(self, house: 'House', price: float | int) -> None:
        self.__money -= price
        self.__house = house
        print("Вы купили дом")

    def _validate_money(self, value: int | float) -> None:
        if not isinstance(value, (int, float)):
            raise ValueError("Укажите числовое значение")

    def earn_money(self, money: int | float):
        self._validate_money(money)

        self.__money += money

    def buy_house(self, house: "House", discount: int):
        price: int = house.final_price(discount)
        if self.__money > price:
            self.__make_deal(house, price)
        else:
            print("Недостаточно денег")


class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount: int) -> float:
        return self._price - (self._price * discount // 100)


class SmallHouse(House):
    def __init__(self, price):
        super().__init__(area=40, price=price)


if __name__ == "__main__":
    user1 = Human("userName", 13)
    user1.earn_money(1000)
    user1.info()
    house1 = House(120, 150)
    print(house1.__dict__)
    user1.buy_house(house1, 50)
    user1.info()
