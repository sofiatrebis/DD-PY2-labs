import doctest
 
class Hotel:
    def __init__(self, total_rooms: int, occupied_rooms: int, payment: float):
        """
        Создание и подготовка к работе объекта "Отель"
 
        :param total_rooms: Общее количество комнат в отеле
        :param occupied_rooms: Количество заселенных комнат
        :param payment: Стоимость одной комнаты
 
        Примеры:
        >>> hotel = Hotel(100, 0, 200.0)  # инициализация экземпляра класса
        """
        
        if not isinstance(total_rooms, int) or total_rooms <= 0:
            raise ValueError("Количество комнат должно натуральным числом")
        
        if not isinstance(occupied_rooms, int) or occupied_rooms < 0:
            raise ValueError("Количество заселенных комнат должно быть целым неотрицательным")
        
        if occupied_rooms > total_rooms:
            raise ValueError("Количество заселенных комнат превышает общюю вместимость")
        
        if not isinstance(payment, (int, float)) or payment <= 0:
            raise ValueError("Стоимость комнаты должна быть положительным числом")
 
    def check_in(self) -> None:
        """
        Заселение человека в отель.
 
        :raise ValueError: Если все комнаты заняты, кидает исключение.
 
        Примеры:
        >>> hotel = Hotel(100, 0, 200.0)
        >>> hotel.check_in()
        """
        if self.occupied_rooms >= self.total_rooms:
            raise ValueError("Все комнаты заняты")
        ...
 
    def check_out(self) -> None:
        """
        Выселение человека из отеля.
 
        :raise ValueError: Если отель пуст, кидает исключение.
 
        Примеры:
        >>> hotel = Hotel(100, 1, 200.0)
        >>> hotel.check_out()
        """
        if self.occupied_rooms <= 0:
            raise ValueError("Отель пуст")
        ...
 
    def daily_income(self) -> float:
        """
        Вычислить ежедневный доход от отеля.
 
        :return: Общий доход от всех заселенных комнат в день.
 
        Примеры:
        >>> hotel = Hotel(100, 2, 200.0)
        >>> hotel.daily_income() # 400.0
        """
        ...
    
 
class Queue:
    def __init__(self, queue_begin):
        """
        Создание и подготовка к работе объекта "Очередь"
 
        :param initial_queue: Список имен в начальной очереди
 
        Примеры:
        >>> queue = Queue(['Иван', 'Рома'])
        """
        if not isinstance(queue_begin, list):
            raise TypeError("initial_queue должен быть списком строк")
        
        for person in queue_begin:
            if not isinstance(person, str):
                raise TypeError("Все элементы в begin должны быть строками")
            
        self.queue = queue_begin
        self.length = len(queue_begin)
 
 
    def person_leaves(self):
        """
        Удаляет человека из начала очереди.
 
        :return: Имя человека, который покинул очередь
        
        Примеры:
        >>> queue = Queue(['Иван', 'Рома'])
        >>> queue.person_leaves()
        'Иван'
        """
        if not self.queue:
            raise IndexError("Очередь пуста")
        ...
 
    def person_joins(self, name):
        """
        Добавляет человека в конец очереди.
 
        :param name: Имя человека, который присоединяется
        
        Примеры:
        >>> queue = Queue(['Иван'])
        >>> queue.person_joins('Рома')
        >>> queue.queue
        ['Иван', 'Рома']
        """
        if not isinstance(name, str):
            raise TypeError("Имя должно быть строкой")
        ...
 
    def get_length(self):
        """
        Возвращает длину очереди.
 
        :return: Длина очереди
        
        Примеры:
        >>> queue = Queue(['Иван', 'Рома'])
        >>> queue.get_length()
        2
        """
        ...
    
 
class Graph:
    def __init__(self, n):
        """
        Создание и подготовка к работе объекта "Граф".
 
        :param n: Количество вершин в графе
 
        Примеры:
        >>> graph = Graph(4)  # инициализация экземпляра класса с 4 вершинами
        """
        if not isinstance(n, int) or n < 0:
            raise ValueError("Количество вершин должно быть целым неотрицательным числом")
        self.n = n 
        self.g = [[False] * n for _ in range(n)]
 
 
    def add_edge(self, u, v):
        """
        Добавление ребра между двумя вершинами. Если ребро уже есть, то ничего не происходит
 
        :param u: Первая вершина
        :param v: Вторая вершина
 
        :raises ValueError: Если номера вершин некорректны
 
        Примеры:
        >>> graph = Graph(4)
        >>> graph.add_edge(0, 1) 
        """
        if not (isinstance(u, int) and isinstance(v, int)):
            raise ValueError("Вершины должны быть целыми числами")
        if not (0 <= u < self.n) or not (0 <= v < self.n):
            raise ValueError(f"Вершины должны быть заданы в диапазоне от 0 до {self.n}")
        ...
 
    def remove_edge(self, u, v):
        """
        Удаление ребра между двумя вершинами.
 
        :param u: Первая вершина
        :param v: Вторая вершина
 
        :raises ValueError: Если одна из вершин за пределами допустимого диапазона
        :raises ValueError: Если ребра не существует
 
        Примеры:
        >>> graph = Graph(4)
        >>> graph.add_edge(0, 1)
        >>> graph.remove_edge(0, 1)
        """
        if not (isinstance(u, int) and isinstance(v, int)):
            raise ValueError("Вершины должны быть целыми числами")
        if not (0 <= u < self.n) or not (0 <= v < self.n):
            raise ValueError(f"Вершины должны быть заданы в диапазоне от 0 до {self.n}")
        
        if self.g[u][v] == 0:
            raise ValueError("Ребра не существует")
        ...
 
    def are_connected(self, u, v):
        """
        Проверяет, соединены ли две вершины ребром.
 
        :param u: Первая вершина
        :param v: Вторая вершина
        :return: True если вершины соединены, иначе False.
 
        Примеры:
        >>> graph = Graph(4)
        >>> graph.add_edge(0, 1)
        >>> graph.are_connected(0, 1)  #  True
        >>> graph.are_connected(1, 2)  #  False
        """
        if not (isinstance(u, int) and isinstance(v, int)):
            raise ValueError("Вершины должны быть целыми числами")
        if not (0 <= u < self.n) or not (0 <= v < self.n):
            raise ValueError(f"Вершины должны быть заданы в диапазоне от 0 до {self.n}")
        ...
 
 
if __name__ == "__main__":
    doctest.testmod()