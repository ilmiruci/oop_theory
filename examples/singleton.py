from typing import Optional


class Odinocka:
    # атрибут класса
    obyekt: Optional['Odinocka'] = None

    # Создает объект класса
    def __new__(cls, *args, **kwargs):
        # print(args, kwargs)

        # if cls.obyekt is None:
        if Odinocka.obyekt is None:
            # Для базового класса говорим, что для
            # текущего класса нужно создать объект
            # noviy_obyekt = super().__new__(cls)
            noviy_obyekt = super().__new__(Odinocka)

            cls.obyekt = noviy_obyekt

        return cls.obyekt

    # Инициализация значений (конструктор класса)
    def __init__(self, name, value):
        # Устанавливает атрибуты для объекта
        self.n = name
        self.v = value
        self.is_valid = True

    def __call__(self, *args, **kwargs):
        print(args, kwargs)
        for arg in args:
            print(arg)

        for key, value in kwargs.items():
            print(key, value)


if __name__ == '__main__':
    s = Odinocka('abc', 123)
    s2 = Odinocka('def', 345)
    s3 = Odinocka('def', 345)
    s4 = Odinocka('def', 345)

    s('ABCDEF', 123, 345, some_var='1224')

    # print(id(s))
    # print(id(s2))
    # print(id(s3))
    # print(id(s4))

    # print(s.n)
    # print(s.v)
