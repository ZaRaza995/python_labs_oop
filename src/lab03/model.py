from validate import validate_name, validate_age, validate_balance

class Patient:
    hospital_name = "Городская больница"

    def __init__(self, name, age, balance=0):
        self._name = validate_name(name)
        self._age = validate_age(age)
        self._balance = validate_balance(balance)
        self._status = "здоров"

    # Свойства 
    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = validate_age(value)

    @property
    def balance(self):
        return self._balance

    @property
    def status(self):
        return self._status

    # Магические методы
    def __str__(self):
        return f"Пациент: {self._name}, Статус: {self._status}"

    def __repr__(self):
        return f"Patient(name='{self._name}', age={self._age}, status='{self._status}', balance={self._balance})"

    def __eq__(self, other):
        if not isinstance(other, Patient):
            return False
        return self._name == other._name and self._age == other._age

    # Бизнес-логика (Состояния)
    def get_sick(self):
        """Пациент заболевает."""
        self._status = "болен"
        print(f"{self._name} теперь в статусе: {self._status}")

    def treat(self):
        """Процесс лечения."""
        if self._status == "здоров":
            print(f"Пациент {self._name} уже здоров, лечение не требуется.")
            return

        if self._balance < 100:
            print(f"Недостаточно средств на балансе ({self._balance}) для лечения!")
            return

        self._balance -= 100
        self._status = "здоров"
        print(f"Пациент {self._name} успешно вылечен! Остаток на балансе: {self._balance}")