from models import Patient, VIPPatient, EmergencyPatient
from collection import Hospital

def demo():
    # Инициализация больницы
    hospital = Hospital()
    
    print("=== Сценарий 1: Разнообразие в приемном покое ===")
    # Создаем пациентов разных типов
    p1 = Patient("Иван", 30, 500)
    vip = VIPPatient("Аркадий", 45, "Др. Хаус", balance=1000, discount=0.2)
    emergency = EmergencyPatient("Петр", 25, balance=300, priority=5, ambulance_id="A777MP")
    
    # Добавляем всех в общую коллекцию
    hospital.add(p1)
    hospital.add(vip)
    hospital.add(emergency)
    
    print(f"Всего пациентов в больнице: {len(hospital)}")
    for p in hospital:
        print(p) # Демонстрация переопределенных __str__
    
    print("\n=== Сценарий 2: Сила Полиморфизма (Массовое лечение) ===")
    # Заставляем всех заболеть
    for p in hospital:
        p.get_sick()
        
    # Лечим всех одним вызовом метода коллекции
    # Здесь сработает разная логика стоимости для каждого типа
    hospital.treat_all_sick()
    
    print("\n=== Сценарий 3: Специфические методы и типизация ===")
    # Ищем только VIP-пациентов через встроенный метод коллекции
    vips = hospital.get_vips()
    print(f"Найдено VIP-персон: {len(vips)}")
    for v in vips:
        # Вызываем уникальный метод, который есть только у VIP
        v.request_personal_doctor()
    
    print("\nРабота со скорой помощью:")
    emer_cases = hospital.get_emergency_patients()
    for em in emer_cases:
        print(f"Меняем приоритет для {em.name}...")
        em.update_priority(1) # Уникальный метод EmergencyPatient
        print(em)

if __name__ == "__main__":
    demo()
