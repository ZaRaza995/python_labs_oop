from model import Patient

class VIPPatient(Patient):
    def __init__(self, name , age,personal_doctor, balance = 0, discount = 0.1):
        super().__init__(name, age, balance)
        self.personal_doctor = personal_doctor
        self.discount = discount

    def __str__(self):
        return f"VIP Пациент: {self._name}, Статус: {self._status}, Доктор: {self.personal_doctor}, Скидка: {self.discount}"
    
    def request_personal_doctor(self):
        print(f"VIP Пациент {self._name} запрашивает консультацию у своего врача {self.personal_doctor}.")
    
    def treat(self):
        actual_cost = 100 * (1 - self.discount)
        if self._balance < actual_cost:
            print(f"У VIP Пациента {self._name} недостаточно средств для лечения (требуется {actual_cost})!")
            return

        self._balance -= actual_cost
        self._status = "здоров"
        print(f"VIP Пациент {self._name} успешно вылечен своим доктором {self.personal_doctor}!")
        print(f"Стоимость со скидкой {self.discount*100}%: {actual_cost}. Остаток: {self._balance}")
        


class EmergencyPatient(Patient):
    
    def __init__(self, name, age, balance = 0, priority = 1, ambulance_id = None):
        super().__init__(name, age, balance)
        self.priority = priority
        self.ambulance_id = ambulance_id

    def __str__(self):
        return f"Экстренный Пациент: {self._name}, Статус: {self._status}, Приоритет: {self.priority}, Машина: {self.ambulance_id}"
    
    def update_priority(self, new_priority):
        self.priority = new_priority
        print(f"Приоритет {self._name} обновлен до {self.priority}")

    def treat(self):
        actual_cost = 150
        if self._balance < actual_cost:
            print(f"У Экстренного Пациента {self._name} недостаточно средств для лечения (требуется {actual_cost})!")
            return

        self._balance -= actual_cost
        self._status = "здоров"
        print(f"Экстренный Пациент {self._name} успешно вылечен!")
        print(f"Стоимость экстренного лечения: {actual_cost}. Остаток: {self._balance}")
