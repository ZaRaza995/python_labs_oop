from model import Patient
class Hospital:
    def __init__(self):
        self._patients = []

    def add(self, patient):
        if isinstance(patient, Patient):
            if patient in self._patients:
                raise ValueError("Такой пациент уже числится в больнице!")
            self._patients.append(patient)
        else:
            raise TypeError("Можно добавлять только объекты Patient")


    def get_all(self):
        return self._patients


    def remove(self, patient):
        if patient in self._patients:
            self._patients.remove(patient)
        else:
            raise ValueError("Пациент не найден в списке")

    def __len__(self):
        return len(self._patients)

    def __iter__(self):
        return iter(self._patients)

    def __getitem__(self, index):
        return self._patients[index]
    
    def find_by_name(self, name):
        for patient in self._patients:
            if patient.name == name:
                return patient 
        return None
    
    def remove_at(self, index):
        if 0 <= index < len(self._patients):
            return self._patients.pop(index)
        else:
            raise IndexError("Индекс вне диапазона")

    def get_sick_patients(self):
        return [patient for patient in self._patients if patient.status == "болен"]
    
    def get_healthy_patients(self):
        return [patient for patient in self._patients if patient.status == "здоров"]

    def sort_by_age(self):
        return sorted(self._patients, key=lambda p: p.age)

