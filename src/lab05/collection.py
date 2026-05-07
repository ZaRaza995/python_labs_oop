class HospitalCollection:
    """Коллекция, поддерживающая функциональный стиль (chaining) и паттерн Стратегия."""

    def __init__(self, items=None):
        # Если элементы не переданы, создаем пустой список
        self._items = items if items is not None else []

    def add(self, item):
        """Добавляет элемент в коллекцию."""
        self._items.append(item)
        return self

    def sort_by(self, key_func, reverse=False):
        """
        Сортирует коллекцию с использованием переданной функции-стратегии.
        Возвращает новую коллекцию для поддержки цепочек вызовов (chaining).
        """
        sorted_items = sorted(self._items, key=key_func, reverse=reverse)
        return HospitalCollection(sorted_items)

    def filter_by(self, predicate_func):
        """
        Фильтрует коллекцию по переданной функции-предикату.
        Возвращает новую коллекцию.
        """
        filtered_items = list(filter(predicate_func, self._items))
        return HospitalCollection(filtered_items)

    def apply(self, func):
        """
        Применяет функцию (или callable-стратегию) ко всем элементам коллекции.
        Меняет текущие элементы, но возвращает self для поддержки chaining.
        """
        for item in self._items:
            func(item)
        return self

    def map_items(self, func):
        """
        Аналог встроенного map(). Возвращает обычный список преобразованных значений.
        """
        return list(map(func, self._items))

    def __iter__(self):
        """Позволяет перебирать коллекцию циклом for."""
        return iter(self._items)

    def print_all(self, title=""):
        """Вспомогательный метод для удобного вывода коллекции."""
        if title:
            print(f"\n--- {title} ---")
        for item in self._items:
            print(item)
        return self
