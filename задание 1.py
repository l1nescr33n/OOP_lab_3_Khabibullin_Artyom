class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.__name = name
        self.__author = author

    def __str__(self):
        return f"Книга {self.__name}. Автор {self.__author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.__name!r}, author={self.__author!r})"

    @property  # Назначаем геттеры и сеттеры, которые помогут проверке и дадут безопасность значениям
    def name_getter(self) -> tuple:
        return self.__name, self.__author

    @name_getter.setter
    def name_getter(self, __name):
        if type(__name) is not str:
            raise TypeError("Введите название книги")

    @property
    def author_getter(self):
        return self.__author

    @author_getter.setter
    def author_getter(self, __author):
        if type(self.__author) is not str:
            raise TypeError("Введите имя автора текстом, либо поставьте прочерк, если автора нет")


class PaperBook(Book):  # Создаём класс PaperBook для работы с количеством страниц

    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)  # Переносим name и author из родительского класса
        self.__name = name
        self.__author = author
        self.__pages = pages

    def __str__(self):
        return f"Книга {self.__name}. Автор {self.__author}. Страницы {self.__pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.__name!r}, author={self.__author!r}, pages={self.__pages!r})"

    @property  # Устанавливаем ограничения для pages и устанавливаем атрибуты неизменными
    def pages_getter(self) -> int:
        return self.__pages

    @pages_getter.setter
    def pages_getter(self, __pages):
        if type(__pages) is not int:
            raise TypeError("Количество страниц должно быть целым числом")
        if __pages <= 0:
            raise ValueError("Количество страниц должно быть больше 0")


class AudioBook(Book):  # Создаём класс AudioBook
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)  # Переносим name и author из родительского класса
        self.__name = name
        self.__author = author
        self.__duration = duration

    @property  # Устанавливаем ограничения для duration и устанавливаем атрибуты неизменными
    def duration_getter(self) -> (int, float):
        return self.__duration

    @duration_getter.setter
    def duration_getter(self, __duration: (float, int)):
        if __duration <= 0:
            raise ValueError("Длительность аудиокниги должна быть больше 0")
        if type(__duration) is not float or int:
            raise TypeError("Длительность аудиокниги должна быть числом")

    def __str__(self):
        return f"Книга {self.__name}. Автор {self.__author}. Продолжительность {self.__duration} мин."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.__name!r}, author={self.__author!r}, duration={self.__duration!r})"


first_book = Book("Гоголь Н.В", "Мёртвые души")  # Объявляем атрибуты класса Book
print(first_book.__str__())  # Печатаем с помощью магического метода __str__
Book.author_getter = "Гоголь Н.В"  # Переназначаем автора и название книги
Book.name_getter = "Вечера на хуторе близ диканьки"
first_book = Book(str(Book.author_getter), str(Book.name_getter))  # Переводим из типа properties в callable
print(first_book.__repr__())  # Печатаем результат с помощью магического метода __repr__

# Примеры с PaperBook и с AudioBook сделаны по тому же принципу, что и Book
second_book = PaperBook("Лермонтов М.Ю", "Мцыри", 100)
print(second_book.__str__())
PaperBook.author_getter = "Лермонтов М.Ю"
PaperBook.name_getter = "Мцыри"
PaperBook.pages_getter = 97
second_book = PaperBook(str(PaperBook.author_getter), str(PaperBook.name_getter), int(PaperBook.pages_getter))
print(second_book.__repr__())

third_book = AudioBook("Пушкин А.С", "Капитанская дочка", 195.6)
print(third_book.__str__())
AudioBook.author_getter = "Пушкин А.С"
AudioBook.name_getter = "Капитанская дочка"
AudioBook.duration_getter = 200.7
third_book = AudioBook(str(AudioBook.author_getter), str(AudioBook.name_getter), float(AudioBook.duration_getter))
print(third_book.__repr__())
