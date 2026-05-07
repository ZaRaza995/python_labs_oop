from models import Patient
from collection import HospitalCollection
import strategies as st

def main():
    print("Демонстрация ЛР-5: Функциональное программирование и Паттерн Стратегия\n" + "="*70)

    # Создаем тестовые данные
    patients = [
        Patient("Иван", 30, 500, "здоров"),
        Patient("Анна", 25, 50, "болен"),
        Patient("Петр", 60, 2000, "болен"),
        Patient("Мария", 18, 0, "болен"),
        Patient("Сергей", 45, 150, "здоров")
    ]

    hospital = HospitalCollection(patients)
    hospital.print_all("Исходная коллекция")

    # --- ДЕМОНСТРАЦИЯ 1: Сортировка тремя разными стратегиями ---
    hospital.sort_by(st.sort_by_name).print_all("Сортировка по имени")
    hospital.sort_by(st.sort_by_age).print_all("Сортировка по возрасту")
    # Используем lambda для быстрой сортировки по балансу
    hospital.sort_by(lambda p: p.balance, reverse=True).print_all("Сортировка по балансу (убывание, через lambda)")


    # --- ДЕМОНСТРАЦИЯ 2: Использование map() и lambda ---
    print("\n--- Извлечение имен всех пациентов через map() ---")
    names = hospital.map_items(lambda p: p.name)
    print(f"Имена: {names}")


    # --- ДЕМОНСТРАЦИЯ 3: Фабрика функций ---
    print("\n--- Фильтрация фабрикой функций (возраст от 20 до 40) ---")
    age_filter_20_40 = st.make_age_filter(20, 40)
    hospital.filter_by(age_filter_20_40).print_all("Пациенты от 20 до 40 лет")


    # --- ДЕМОНСТРАЦИЯ 4: СЦЕНАРИЙ 1 (Полная цепочка операций) ---
    print("\n" + "="*50)
    print("СЦЕНАРИЙ 1: Полная цепочка filter -> sort -> apply")
    # Задача: найти всех больных с деньгами, отсортировать по возрасту и вылечить
    treat_strategy = st.TreatStrategy(cost=100)
    
    (hospital
        .filter_by(st.is_sick)                  # 1. Фильтруем только больных
        .filter_by(st.is_solvent)               # 2. Фильтруем только тех, у кого есть деньги
        .sort_by(st.sort_by_age)                # 3. Сортируем по возрасту
        .print_all("Перед лечением (отфильтрованы и отсортированы)")
        .apply(treat_strategy)                  # 4. Применяем callable-стратегию лечения
        .print_all("После применения стратегии лечения")
    )


    # --- ДЕМОНСТРАЦИЯ 5: СЦЕНАРИЙ 2 (Замена стратегии) ---
    print("\n" + "="*50)
    print("СЦЕНАРИЙ 2 и 3: Замена стратегии на лету и callable-объекты")
    
    # Создаем новую независимую коллекцию
    new_hospital = HospitalCollection([Patient("Олег", 40, 1000, "здоров"), Patient("Яна", 20, 100, "здоров")])
    new_hospital.print_all("Новые пациенты")

    # Применяем одну стратегию (обычная функция)
    new_hospital.apply(st.make_sick)
    new_hospital.print_all("После применения стратегии 'make_sick' (стали больными)")

    # Меняем стратегию на другую (callable объект) без изменения кода коллекции
    bonus_strategy = st.ApplyDiscountStrategy(bonus_amount=500)
    new_hospital.apply(bonus_strategy)
    new_hospital.print_all("После замены стратегии на 'ApplyDiscountStrategy' (выдан бонус 500)")

if __name__ == "__main__":
    main()
