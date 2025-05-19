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
    __letters_num: int = 26

    def __init__(self) -> None:
        super().__init__(language="En", letters=string.ascii_uppercase)

    def is_in_letter(self, letter: str) -> bool:
        return letter.upper() in self.letters

    def letters_num(self) -> int:
        return self.__letters_num

    @staticmethod
    def example():
        return ("Alice was beginning to get very tired of sitting by her sister on \n"
                "the bank, and of having nothing to do: once or twice she had peeped \n"
                "into the book her sister was reading, but it had no pictures or conversations \n"
                "in it, \"and what is the use of a book,\" thought Alice \"without pictures or conversation?")



if __name__ == "__main__":
    en = EngAlphabet()
    en.print()
    print(en.letters_num())
    print(en.is_in_letter("F"))
    print(en.is_in_letter("Щ"))
    print(en.example())
