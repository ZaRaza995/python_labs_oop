from model import Patient
from collection import Hospital

# Создание больницы
hospital = Hospital()

# создание пациентов
p1 = Patient("Иван", 30, 1000)
p2 = Patient("Мария", 25, 500)
p3 = Patient("Петр", 35, 200)

hospital.add(p1)
hospital.add(p2)
hospital.add(p3)

print(f"Количество пациентов в больнице: {len(hospital)}")

for patient in hospital:
    print(patient)

try:
    hospital.add(p1)
except ValueError as e:
    print(f"Ошибка добавления: {e}")

print("\n --- Сценарий 2 ---")

ivan = hospital.find_by_name("Иван")
ivan.get_sick()

sick_list = hospital.get_sick_patients()
print("Список больных пациентов:")
for sick_patient in sick_list:
    print(sick_patient)

print("\n --- Сценарий 3 ---")
# 1. Проверяем сортировку
sorted_patients = hospital.sort_by_age()
print(f"Самый молодой пациент: {sorted_patients[0].name} ({sorted_patients[0].age} лет)")

# 2. Проверяем наш метод индексации __getitem__ (получаем нулевого пациента прямо из объекта больницы)
print(f"Первый добавленный пациент в базе: {hospital[0].name}")

# 3. Лечим Ивана (проверка бизнес-логики из ЛР-1)

print("\nОформляем лечение Ивану...")
ivan.treat()

# 4. Проверяем удаление по индексу (выписываем первого пациента)
print("\nВыписываем (удаляем) самого первого пациента в списке...")
hospital.remove_at(0)

print("Оставшиеся пациенты в больнице:")
for p in hospital:
    print(p)




















