class Patient:
    """Базовый класс пациента с аннотациями типов."""
    def __init__(self, name: str, age: int, balance: float) -> None:
        self._name: str = name
        self._age: int = age
        self._balance: float = balance

    def get_name(self) -> str:
        return self._name

    def get_age(self) -> int:
        return self._age
        
    def get_balance(self) -> float:
        return self._balance

    def display(self) -> str:
        return f"[Пациент] {self._name}, Возраст: {self._age}"

    def get_bill_amount(self) -> float:
        return 500.0


class VIPPatient(Patient):
    def __init__(self, name: str, age: int, balance: float, discount: float) -> None:
        super().__init__(name, age, balance)
        self._discount: float = discount

   
    def display(self) -> str:
        return f"[VIP Пациент] {self._name}, Скидка: {int(self._discount * 100)}%"

 
    def get_bill_amount(self) -> float:
        return 500.0 * (1.0 - self._discount)


class Doctor:
    """Класс Врача. Он не является Пациентом, но тоже умеет display()."""
    def __init__(self, name: str, specialty: str) -> None:
        self._name: str = name
        self._specialty: str = specialty

    def display(self) -> str:
        return f"[Врач] {self._name}, Специальность: {self._specialty}"
