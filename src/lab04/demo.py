from models import Patient, Doctor
from interfaces import Printable, Comparable
from collection import HospitalCollection

# --- Универсальная функция ---
def print_all(items: list[Printable]):
    """Функция работает исключительно через интерфейс Printable."""
    print("\n--- Вывод через универсальную функцию ---")
    for item in items:
        # Без `if isinstance(obj, A)` - чистый полиморфизм
        print(item.to_string())

def main():
    print("Демонстрация ЛР-4: Интерфейсы и абстрактные классы\n" + "="*50)

    # 1. Создание объектов
    p1 = Patient("Иван Пациентов", 30, 500)
    p2 = Patient("Анна Больная", 25, 100)
    d1 = Doctor("Петр Врачев", "Хирург", 15)
    d2 = Doctor("Мария Докторова", "Терапевт", 5)

    # 2. Демонстрация: объект реализует несколько интерфейсов и проверка isinstance
    print(f"p1 реализует Printable? {isinstance(p1, Printable)}")
    print(f"p1 реализует Comparable? {isinstance(p1, Comparable)}")
    print(f"d1 реализует Printable? {isinstance(d1, Printable)}")

    # 3. Универсальная функция (работа с объектами разных типов)
    mixed_list = [p1, d1, p2, d2]
    print_all(mixed_list)

    # 4. Работа с Коллекцией 
    hospital = HospitalCollection()
    hospital.add_item(p1)
    hospital.add_item(p2)
    hospital.add_item(d1)
    hospital.add_item(d2)
    # Добавим объект, который не имеет интерфейсов вообще, чтобы показать фильтрацию
    hospital.add_item("Просто случайная строка") 

    print("\n--- Фильтрация коллекции по интерфейсу Printable ---")
    printables = hospital.get_printables()
    for item in printables:
        print(f"Найдено: {item.to_string()}")

    print("\n--- Архитектурное поведение: Сортировка через интерфейс Comparable ---")
    # Получаем только пациентов для сравнения между собой
    patients_only = [item for item in hospital.get_comparables() if isinstance(item, Patient)]
    sorted_patients = hospital.sort_comparables(patients_only)
    
    print("Пациенты до сортировки (по добавлению):")
    for p in patients_only:
        print(p.to_string())
        
    print("\nПациенты после сортировки (по возрасту, благодаря compare_to):")
    for p in sorted_patients:
        print(p.to_string())

if __name__ == "__main__":
    main()
