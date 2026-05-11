from models import Patient, VIPPatient, Doctor
from container import TypedCollection, Displayable, Billable

def main() -> None:
    print("Демонстрация ЛР-6: Типизация, Generic и Protocol\n" + "="*50)

    print("\n--- 1. Работа TypedCollection[Patient] ---")
    patients: TypedCollection[Patient] = TypedCollection()
    
    p1 = Patient("Иван", 30, 1000.0)
    p2 = Patient("Анна", 25, 500.0)
    vip1 = VIPPatient("Олег", 40, 2000.0, discount=0.2)
    
    patients.add(p1)
    patients.add(p2)
    patients.add(vip1) # VIPPatient - наследник Patient, поэтому всё ок

    # find()
    found: Patient | None = patients.find(lambda p: p.get_age() == 25)
    print(f"Найден 25-летний пациент: {found.get_name() if found else 'Не найден'}")
    
    not_found: Patient | None = patients.find(lambda p: p.get_age() == 99)
    print(f"Найден 99-летний пациент: {not_found}")

    # filter()
    rich_patients: list[Patient] = patients.filter(lambda p: p.get_balance() >= 1000.0)
    print(f"Пациенты с балансом >= 1000: {[p.get_name() for p in rich_patients]}")

    names: list[str] = patients.map(lambda p: p.get_name())
    balances: list[float] = patients.map(lambda p: p.get_balance())
    print(f"Список имён (list[str]): {names}")
    print(f"Список балансов (list[float]): {balances}")



    print("\n\n--- 2. Сценарий 1: Protocol Displayable ---")

    displayables: TypedCollection[Displayable] = TypedCollection()
    
    displayables.add(Patient("Мария", 22, 100.0))
    displayables.add(VIPPatient("Петр", 55, 3000.0, 0.5))
    displayables.add(Doctor("Айболит", "Ветеринар"))

    for item in displayables.get_all():
        print(item.display())


    print("\n--- 3. Сценарий 2: Protocol Billable ---")
    billables: TypedCollection[Billable] = TypedCollection()
    
    billables.add(Patient("Игорь", 33, 0.0))
    billables.add(VIPPatient("Жанна", 44, 0.0, 0.1))
    

    total_bill: float = 0.0
    for client in billables.get_all():
        bill = client.get_bill_amount()
        total_bill += bill
        print(f"К оплате клиентом: {bill}")
    
    print(f"Итого выставлено счетов: {total_bill}")


if __name__ == "__main__":
    main()
