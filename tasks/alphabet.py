import string

class Alphabet:
    def __init__(self, language: str, letters: str):
        self.lang: str = language
        self.letters: str = letters

    def print(self) -> None:
        print(self.letters)

    def letters_num(self) -> int:
        return len(self.letters)

class EngAlphabet(Alphabet):
    def __init__(self) -> None:
        super().__init__(language="En", letters=string.ascii_uppercase)
        self.__letters_num = len(self.letters)

    def is_in_letter(self, letter: str):
        if letter.upper() in self.letters:
            print(f"Буква {letter} есть в алфавите")
        else:
            print(f"Буквы {letter} нет в алфавите")

    def letters_num(self) -> int:
        return self.__letters_num

    @staticmethod
    def example(self):
        pass



if __name__ == "__main__":
    en = EngAlphabet()
    en.print()
    print(en.letters_num())
    en.is_in_letter("F")
    en.is_in_letter("Щ")
    print(en.__dict__)
