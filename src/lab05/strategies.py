"""
В этом файле хранятся все функции высшего порядка, стратегии фильтрации, 
сортировки и обработки (паттерн Стратегия).
"""

# --- СТРАТЕГИИ СОРТИРОВКИ ---
def sort_by_name(patient):
    """Стратегия сортировки по имени."""
    return patient.name

def sort_by_age(patient):
    """Стратегия сортировки по возрасту."""
    return patient.age

def sort_by_balance_and_age(patient):
    """Стратегия сортировки по балансу (по убыванию), а затем по возрасту."""
    return (-patient.balance, patient.age)


# --- СТРАТЕГИИ ФИЛЬТРАЦИИ ---
def is_sick(patient):
    """Фильтр: только больные пациенты."""
    return patient.status == "болен"

def is_solvent(patient):
    """Фильтр: пациенты с положительным балансом (могут оплатить лечение)."""
    return patient.balance > 0

# --- ФАБРИКА ФУНКЦИЙ (Замыкание) ---
def make_age_filter(min_age: int, max_age: int):
    """
    Фабрика функций. Создает и возвращает функцию-фильтр, 
    которая проверяет, попадает ли пациент в заданный возрастной диапазон.
    """
    def filter_fn(patient):
        return min_age <= patient.age <= max_age
    return filter_fn


# --- ПАТТЕРН СТРАТЕГИЯ ЧЕРЕЗ CALLABLE-ОБЪЕКТЫ ---
class TreatStrategy:
    """
    Стратегия лечения (callable-объект).
    Списывает фиксированную стоимость лечения и меняет статус на 'здоров'.
    """
    def __init__(self, cost: float):
        self.cost = cost

    def __call__(self, patient):
        if patient.status == "болен" and patient.balance >= self.cost:
            patient.balance -= self.cost
            patient.status = "здоров"
            print(f"Вылечен: {patient.name} (списано {self.cost})")
        return patient

class ApplyDiscountStrategy:
    """
    Стратегия начисления бонуса/скидки (callable-объект).
    """
    def __init__(self, bonus_amount: float):
        self.bonus_amount = bonus_amount

    def __call__(self, patient):
        patient.balance += self.bonus_amount
        return patient

# --- ОБЫЧНЫЕ ФУНКЦИИ-ОБРАБОТЧИКИ (для apply) ---
def make_sick(patient):
    """Функция-стратегия, которая делает пациента больным."""
    patient.status = "болен"
    return patient
