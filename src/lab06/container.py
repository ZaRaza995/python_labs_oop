from typing import TypeVar, Generic, Callable, Optional, Protocol

# 1. Определение протоколов (структурных интерфейсов)
class Displayable(Protocol):
    """Протокол для объектов, которые можно отобразить в виде строки."""
    def display(self) -> str:
        ...

class Billable(Protocol):
    """Протокол для объектов, которым можно выставить счет."""
    def get_bill_amount(self) -> float:
        ...

# 2. Определение TypeVar
# T - обычный любой тип
T = TypeVar('T')
# R - тип для результата метода map
R = TypeVar('R')
# D - тип, который строго ограничен протоколом Displayable
D = TypeVar('D', bound=Displayable)
# B - тип, ограниченный протоколом Billable
B = TypeVar('B', bound=Billable)


# 3. Реализация Generic коллекции
class TypedCollection(Generic[T]):
    """Строго типизированная коллекция."""
    
    def __init__(self) -> None:
        self._items: list[T] = []

    def add(self, item: T) -> None:
        self._items.append(item)

    def remove(self, item: T) -> None:
        self._items.remove(item)

    def get_all(self) -> list[T]:
        return list(self._items)

    # --- Новые методы из требований на 4 ---

    def find(self, predicate: Callable[[T], bool]) -> Optional[T]:
        """Возвращает первый подходящий элемент или None."""
        for item in self._items:
            if predicate(item):
                return item
        return None

    def filter(self, predicate: Callable[[T], bool]) -> list[T]:
        """Возвращает список всех подходящих элементов."""
        return [item for item in self._items if predicate(item)]

    def map(self, transform: Callable[[T], R]) -> list[R]:
        """Применяет функцию ко всем элементам, меняя тип результата (R)."""
        return [transform(item) for item in self._items]
