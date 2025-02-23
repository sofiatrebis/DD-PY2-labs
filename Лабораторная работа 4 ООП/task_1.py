class Device:
    """ Базовый класс устройства. """
    def __init__(self, username: str, ip_address: str, operating_system: str, memory: float):
        self._username = username  # Имя пользователя - защищенный атрибут
        self._ip_address = ip_address  # IP адрес - защищенный атрибут
        self.operating_system = operating_system
        self.memory = memory

    @property
    def username(self) -> str:
        """ Свойство,возвращающее имя пользователя """
        return self._username

    @property
    def ip(self) -> str:
        """ Свойство,возвращающее IP компьютера """
        return self._ip_address

    def __str__(self) -> str:
        return (
            f'Компьютер пользователя {self._username}. IP адрес {self._ip_address}. '
            f'Операционная система {self.operating_system}. Вместимость памяти: {self.memory} Гб'
                )

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}(username={self._username!r}, ip_address={self._ip_address!r}, "
            f"operating_system={self.operating_system!r}, memory={self.memory!r})"
        )

    def programm_installed(self, programm_weight: float) -> str:
        """
        Метод, проверяющий, возможно ли установить программу на устройство
        :param programm_weight: вес программы в Гб
        :return: строка с информацией о том, возможно ли установить программу
        """
        if self.memory >= programm_weight:
            return f'Установка программы доступна.'
        else:
            return f'Невозможно установить программу. Требуется: {programm_weight} Гб, доступно {self.memory} Гб'

    def operating_system_update(self, latest_operating_system: str):
        """
        Метод, проверяющий, возможно ли обновить ОС
        :param latest_operating_system: последняя версия ОС
        :return: строка с информацией о том, возможно ли обновить ОС
        """
        if latest_operating_system == self.operating_system:
            return f'У вас уже установлена последняя версия ОС: {self.operating_system}'
        else:
            return f'Текущая версия ОС: {self.operating_system}. Возможно обновить до {latest_operating_system}'


class Computer(Device):
    """ Класс описывающий компьютер """
    def __init__(self, username: str, ip_address: str, operating_system: str, memory: float, storage_type: str):
        """
        Конструктор класса компьютер
        :param username: имя пользователя
        :param ip_address: IP адрес компьютера
        :param operating_system: ОС компьютера
        :param memory: количество свободной памяти в Гб
        :param storage_type: тип накопителя
        """
        super().__init__(username, ip_address, operating_system, memory)
        self.storage_type = storage_type

    def __str__(self) -> str:
        return f"{super().__str__()}. Тип накопителя {self.storage_type}"

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}(username={self._username!r}, ip_address={self._ip_address!r}, "
            f"operating_system={self.operating_system!r}, memory={self.memory!r}, storage_type={self.storage_type!r})"
        )

    def programm_installed(self, programm_weight: float, is_admin: bool) -> str:
        """
        Перегруженный метод проверяет, достаточно ли памяти и обладает ли пользователь правами администратора
        :param programm_weight: вес программы в Гб
        :param is_admin: параметр, хранящий информацию о том, обладает ли пользователь правами администратора
        :return: строка с информацией о том, возможно ли установить программу
        """
        if is_admin:
            if self.memory >= programm_weight:
                return f'Установка программы доступна.'
            else:
                return f'Невозможно установить программу. Требуется: {programm_weight} Гб, доступно {self.memory} Гб'
        else:
            return f'Невозможно установить программу. Требуется войти от имени администратора'


class Smartphone(Device):
    """ Класс описывающий смартфон """
    def __init__(self, username: str, ip_address: str, operating_system: str, memory: float, battery_life: float):
        """
        Конструктор класса смартфон
        :param username: имя пользователя
        :param ip_address: IP адрес компьютера
        :param operating_system: ОС компьютера
        :param memory: количество свободной памяти в Гб
        :param battery_life: оставшийся заряд батареи
        """
        super().__init__(username, ip_address, operating_system, memory)
        self.battery_life = battery_life

    def __str__(self) -> str:
        return f"{super().__str__()}. Оставшийся заряд батареи {self.battery_life}"

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}(username={self._username!r}, ip_address={self._ip_address!r}, "
            f"operating_system={self.operating_system!r}, memory={self.memory!r}, battery_life={self.battery_life!r})"
        )

    def programm_installed(self, programm_weight: float) -> str:
        """
        Перегруженный метод проверяет, достаточно ли памяти и достаточно ли заряда батареи
        :param programm_weight: вес программы в Гб
        :return: строка с информацией о том, возможно ли установить программу
        """
        if self.battery_life > 0:
            if self.memory >= programm_weight:
                return f'Установка программы доступна.'
            else:
                return f'Невозможно установить программу. Требуется: {programm_weight} Гб, доступно {self.memory} Гб'
        else:
            return f'Невозможно установить программу. Недостаточно заряда батареи'


if __name__ == '__main__':
    device = Device('Nikita', '106.73.209.98', 'macOS 14.2.1', 500)
    print(device)
    print(device.programm_installed(40.0))
    print(device.operating_system_update('macOS 15.1.1'))

    computer = Computer('Sonic', '106.73.209.98', 'Windows 10', 100, 'SSD')
    print(computer)
    print(computer.programm_installed(112.0, False))
    print(computer.operating_system_update('Windows 11'))

    smartphone = Smartphone('Lunas iPhone', '106.73.209.98', 'iOS 17.0', 54.0, 25.0)
    print(smartphone)
    print(smartphone.programm_installed(30.0))
    print(smartphone.operating_system_update('iOS 17.0'))
