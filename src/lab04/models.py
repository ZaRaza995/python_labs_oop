from interfaces import Printable, Comparable

# --- Вспомогательные функции валидации ---
def validate_name(name):
    if not isinstance(name, str) or not name.strip():
        raise ValueError("Имя должно быть непустой строкой")
    return name.strip()

def validate_age(age):
    if not isinstance(age, int) or not (0 <= age <= 120):
        raise ValueError("Возраст должен быть целым числом от 0 до 120")
    return age

# --- Модели ---

class Patient(Printable, Comparable):
    """Класс Пациента, реализующий два интерфейса."""
    
    def __init__(self, name: str, age: int, balance: float = 0):
        self._name = validate_name(name)
        self._age = validate_age(age)
        self._balance = balance
        self._status = "здоров"

    @property
    def name(self): return self._name

    @property
    def age(self): return self._age
    
    @property
    def balance(self): return self._balance

    # Реализация интерфейса Printable
    def to_string(self) -> str:
        return f"[Пациент] {self._name}, {self._age} лет. Баланс: {self._balance}"

    # Реализация интерфейса Comparable (сравнение пациентов по возрасту)
    def compare_to(self, other) -> int:
        if not isinstance(other, Patient):
            raise TypeError("Пациента можно сравнивать только с другим пациентом")
        
        if self._age < other._age:
            return -1
        elif self._age > other._age:
            return 1
        return 0


class Doctor(Printable, Comparable):
    """Класс Врача, реализующий два интерфейса (по-своему)."""
    
    def __init__(self, name: str, specialty: str, experience_years: int):
        self._name = validate_name(name)
        self._specialty = specialty
        self._experience = experience_years

    @property
    def name(self): return self._name

    @property
    def experience(self): return self._experience

    # Реализация интерфейса Printable (другая реализация)
    def to_string(self) -> str:
        return f"[Врач] {self._name}, Специальность: {self._specialty}, Стаж: {self._experience} лет"

    # Реализация интерфейса Comparable (сравнение врачей по стажу)
    def compare_to(self, other) -> int:
        if not isinstance(other, Doctor):
            raise TypeError("Врача можно сравнивать только с другим врачом")
        
        if self._experience < other._experience:
            return -1
        elif self._experience > other._experience:
            return 1
        return 0
