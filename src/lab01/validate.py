def validate_name(name):
    if not isinstance(name, str) or not name.strip():
        raise ValueError("Имя должно быть непустой строкой")
    return name.strip()

def validate_age(age):
    if not isinstance(age, int):
        raise ValueError("Возраст должен быть целым числом")
    if not (0 <= age <= 120):
        raise ValueError("Возраст должен быть в диапазоне от 0 до 120")
    return age

def validate_balance(balance):
    if not isinstance(balance, (int, float)):
        raise ValueError("Баланс должен быть числом")
    if balance < 0:
        raise ValueError("Баланс не может быть отрицательным")
    return balance
