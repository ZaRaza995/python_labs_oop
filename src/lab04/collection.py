from interfaces import Printable, Comparable

class HospitalCollection:
    """Коллекция (из требований на 5), управляющая объектами через интерфейсы."""
    
    def __init__(self):
        self._items = []

    def add_item(self, item):
        """Добавляет любой объект в коллекцию."""
        self._items.append(item)

    def get_printables(self) -> list[Printable]:
        """Фильтрация: возвращает только те объекты, которые реализуют Printable."""
        return [item for item in self._items if isinstance(item, Printable)]

    def get_comparables(self) -> list[Comparable]:
        """Фильтрация: возвращает только те объекты, которые реализуют Comparable."""
        return [item for item in self._items if isinstance(item, Comparable)]

    def sort_comparables(self, items: list[Comparable]) -> list[Comparable]:
        """Архитектурное поведение: сортировка коллекции через интерфейс Comparable.
        Используется пузырьковая сортировка для наглядного применения compare_to."""
        n = len(items)
        # Копируем список, чтобы не менять оригинал
        sorted_items = items.copy()
        
        for i in range(n):
            for j in range(0, n - i - 1):
                # Полиморфизм: мы не знаем классы объектов, мы просто дергаем интерфейс compare_to
                if sorted_items[j].compare_to(sorted_items[j + 1]) == 1:
                    sorted_items[j], sorted_items[j + 1] = sorted_items[j + 1], sorted_items[j]
                    
        return sorted_items
