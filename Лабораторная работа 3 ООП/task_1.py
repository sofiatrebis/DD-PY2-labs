class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        """ Свойство,возвращающее название книги """
        return self._name

    @property
    def author(self) -> str:
        """ Свойство,возвращающее автора книги """
        return self._author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook (Book):
    """ Класс описывающий бумажную книгу """
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        if not isinstance(pages, int):
            raise TypeError('Количество страниц должно быть типа int')
        if pages <= 0:
            raise ValueError('Количество страниц должно быть > 0')
        self._pages = pages

    def __str__(self):
        return f"{super().__str__()}. Количество страниц {self._pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self._pages!r})"

    @property
    def pages(self) -> int:
        """ Свойство,возвращающее количество страниц """
        return self._pages

    @pages.setter
    def pages(self, new_pages: int) -> None:
        """ Устанавливает новое количество страниц """
        if not isinstance(new_pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if new_pages <= 0:
            raise ValueError("Количество страниц должно быть > 0")
        self._pages = new_pages


class AudioBook(Book):
    """ Класс описывающий аудиокнигу """
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        if not isinstance(duration, float):
            raise TypeError('Длительность книги должна быть типа float')
        if duration <= 0:
            raise ValueError("Длительность должна быть > 0")
        self._duration = duration

    def __str__(self):
        return f"{super().__str__()}. Длительность {self._duration}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self._duration!r})"

    @property
    def duration(self) -> float:
        """ Свойство,возвращающее длительность книги """
        return self._duration

    @duration.setter
    def duration(self, new_duration: float) -> None:
        """ Устанавливает новую длительность книги """
        if not isinstance(new_duration, float):
            raise TypeError("Длительность книги должна быть типа float")
        if new_duration <= 0:
            raise ValueError("Длительность книги должна быть > 0")
        self._duration = new_duration


if __name__ == '__main__':
    book = Book('The Great Gatsby', 'Fitzgerald')
    print(book)

    paper_book = PaperBook('The Iliad', 'Homer', 350)
    print(paper_book)

    audio_book = AudioBook('Hamlet', 'Shakespeare', 8.0)
    print(repr(audio_book))
