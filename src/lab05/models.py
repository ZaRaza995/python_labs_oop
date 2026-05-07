class Patient:
    """Класс Пациента из предыдущих ЛР."""
    
    def __init__(self, name: str, age: int, balance: float = 0, status: str = "здоров"):
        self._name = name
        self._age = age
        self._balance = balance
        self._status = status

    @property
    def name(self): return self._name

    @property
    def age(self): return self._age
    
    @property
    def balance(self): return self._balance

    @property
    def status(self): return self._status

    @status.setter
    def status(self, value): self._status = value

    @balance.setter
    def balance(self, value): self._balance = value

    def __str__(self) -> str:
        return f"[Пациент] {self._name}, {self._age} лет. Баланс: {self._balance}. Статус: {self._status}"

    def __repr__(self) -> str:
        return self.__str__()
